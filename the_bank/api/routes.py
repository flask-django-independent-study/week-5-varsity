"""Import libraries."""
from flask import Blueprint, request, jsonify

# HERE: we import auth_required. This allows us to decorate the routes or
# API endpoints we want only want logged in users to access
from flask_praetorian import auth_required

# HERE: we import guard from our __init__.py file. guard has methods such as
# authenticate, hash_password, and encode_jwt_token which we will use
from the_bank import db, guard
from the_bank.models import Account

api = Blueprint("api", __name__)

# NOTE: I have taken care of the JavaScript for you. If you are unsure what
# the routes receive, peek into the main.js file to see how it all works

# NOTE: Additionally, try testing each route either through the front-end or
# using Postman. Remember, its easiest to test as you go rather than testing
# everything at the end.


@api.route("/account", methods=["GET"])
def get_all_accounts():
    """Get all open accounts."""
    accounts = Account.query.all()
    print(accounts)
    return ""


@api.route("/account", methods=["POST"])
def open_account():
    """Open a new account."""
    # TODO: refactor this endpoint be secure
    # HINT: this route should hash the password before it is saved
    holder = request.json.get("holder")
    account = Account.query.filter_by(holder=holder).first()
    if account:
        return jsonify({"error": "Account already exists"})
    account = Account(holder=holder)
    db.session.add(account)
    db.session.commit()
    return (
        jsonify(
            {"message": f"An account for {account.holder} has been created"}
        ),
        201,
    )


# HERE: we changed the method to view_account from POST to PUT. We also
# removed the dynamic route. This allows us to pass both the holder and the
# password through the request body. This is a more secure way of sending data.
# We wouldn't want either or both of the holder and account to be visible on
# the url.
@api.route("/account", methods=["PUT"])
def view_account():
    """View an account."""
    # TODO: refactor this endpoint use tokens
    # HINT: this route should authenticate the password then return a token
    # along with the holder and balance
    account = Account.query.filter_by(holder=holder).first()
    if account:
        return (
            jsonify({"holder": account.holder, "balance": account.balance}),
            200,
        )
    return jsonify({"error": "Account does not exist"})


# HERE: similar to view_account, we remove the dynamic route in favor of
# passing the data through the request body:
@api.route("/account", methods=["DELETE"])
def close_account():
    """Close an account."""
    # TODO: refactor this endpoint be secure
    # HINT: we need to authenticate the password and only closed the account
    # if the password is correct
    account = Account.query.filter_by(holder=holder).first()
    if not account:
        return jsonify({"error": "Account does not exist"})
    if account.balance > 0:
        return jsonify({"error": "Remove balance before closing account"})
    db.session.delete(account)
    db.session.commit()
    return jsonify({"message": "The account has been closed"})


# TODO: allow only logged in users to access this endpoint
@api.route("/account/<holder>/deposit", methods=["POST"])
def deposit(holder):
    """Deposit to account of a given holder."""
    account = Account.query.filter_by(holder=holder).first()
    if not account:
        return jsonify({"error": "Account does not exist"})
    amount = request.json.get("amount")
    account.balance += amount
    db.session.commit()
    return jsonify(
        {
            "holder": account.holder,
            "balance": account.balance,
            "message": "The deposit has been processed",
        }
    )


# TODO: allow only logged in users to access this endpoint
@api.route("/account/<holder>/withdraw", methods=["POST"])
def withdraw(holder):
    """Withdraw from account of a given holder."""
    account = Account.query.filter_by(holder=holder).first()
    amount = request.json.get("amount")
    if not account:
        return jsonify({"error": "Account does not exist"})
    if account.balance >= amount:
        account.balance -= amount
        db.session.commit()
        return jsonify(
            {
                "holder": account.holder,
                "balance": account.balance,
                "message": "The withdraw has been processed",
            }
        )
    return jsonify({"error": "The account balance is insufficient"})
