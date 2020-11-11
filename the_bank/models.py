"""Import libraries."""
from the_bank import db


class Account(db.Model):
    """Account database model class."""

    id = db.Column(db.Integer, primary_key=True)
    holder = db.Column(db.String(100), nullable=False, unique=True)
    # TODO: add a password column that is of type Text
    balance = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        """Return account holder."""
        return f"Account('{self.holder}')"

    # HERE: we see four new methods. Two property methods and two class methods.
    # These methods were taken straight out of the docs and changed to fit our
    # needs. The reason why we need them is flask-praetorian specifically looks
    # for and calls these methods at different point in the authentication
    # process. With this in mind, naming and spelling of the method names are
    # important.

    # identity is a property method that returns the account id
    @property
    def identity(self):
        return self.id

    # rolenames is a property method that returns the roles of the class, in
    # this case, account. We don't have any roles for our account. This would
    # be important, for instance, if we had an admin role hat we wanted to let
    # access additional parts of the app, and we had a customer role that we
    # wanted to restrict access to certain parts of the app.
    @property
    def rolenames(self):
        return []

    # lookup is a class method which takes in the class "cls" and holder. It
    # returns an account that matches the holder which is passed in.
    @classmethod
    def lookup(cls, holder):
        return cls.query.filter_by(holder=holder).one_or_none()

    # identify is a class method which takes in the class "cls" and id. It
    # returns an account that matches the id which is passed in.
    @classmethod
    def identify(cls, id):
        return cls.query.get(id)


# TODO: go to the-bank/__init__.py
