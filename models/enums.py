import enum

class RoleType(enum.Enum):
    approver = "approver"
    complainer = "complainer"
    admin = "admin"

class State(enum.Enum):
    pending = "Pending"
    approver = "Approved"
    rejected = "Rejected"

    #sqlalchemy.Column("role",   sqlalchemy.Enum(RoleType), nullable=False, server_default=RoleType.complainer.name),
   # sqlalchemy.Column("status", sqlalchemy.Enum(State),    nullable=False, server_defalut=State.pending.name),
