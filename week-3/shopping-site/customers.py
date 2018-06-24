"""Customers at Hackbright."""


class Customer(object):
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        # TODO: need to implement this

    def __repr__(self):
        return "<{} {}: {}, {}>".format(self.first_name, self.last_name,
                                        self.email, self.password)


def create_customer_dict(file):
    email_dict = {}
    file_input = open(file)
    for line in file_input:
        line = line.rstrip().split("|")
        f_name, l_name, email, pword = line
        email_dict[email] = Customer(f_name, l_name, email, pword)

    return email_dict


def get_by_email(email):
    return email_dict.get(email)


email_dict = create_customer_dict('customers.txt')
