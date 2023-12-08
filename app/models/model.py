import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, mapped_column

Base = declarative_base()


# pylint: disable-next=too-few-public-methods
class LivestockProductDB(Base):
    __tablename__ = "livestock_product"
    id = mapped_column(sa.Integer, primary_key=True)
    livestock_id = mapped_column(sa.UUID(as_uuid=True), nullable=False)
    product_id = mapped_column(sa.Integer, nullable=False)

    # pylint: disable-next=too-few-public-methods
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "livestock_id": self.type,
            "product_id": self.name,
        }
