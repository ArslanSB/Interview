from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List, TYPE_CHECKING
from database import Base

if TYPE_CHECKING:
    from domain import Client, Address


class ClientModel(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    
    # Relación: un cliente puede tener múltiples direcciones
    addresses: Mapped[List["AddressModel"]] = relationship(
        "AddressModel", 
        back_populates="client",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<ClientModel(id={self.id}, name={self.name}, email={self.email})>"
    
    def to_domain(self, include_addresses: bool = True) -> "Client":
        """Convierte la entidad de base de datos a modelo de dominio
        
        Args:
            include_addresses: Si True, incluye las direcciones relacionadas
        """
        from domain import Client
        
        addresses_domain = []
        if include_addresses and self.addresses:
            addresses_domain = [addr.to_domain() for addr in self.addresses]
        
        return Client(
            id=self.id,
            name=self.name,
            email=self.email,
            phone=self.phone,
            created_at=self.created_at,
            addresses=addresses_domain
        )


class AddressModel(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False
    )
    address_type: Mapped[str] = mapped_column(
        String(50), 
        nullable=False  # 'home', 'billing', 'shipping', etc.
    )
    street: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(100), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    
    # Relación inversa
    client: Mapped["ClientModel"] = relationship("ClientModel", back_populates="addresses")

    def __repr__(self) -> str:
        return f"<AddressModel(id={self.id}, client_id={self.client_id}, type={self.address_type})>"
    
    def to_domain(self) -> "Address":
        """Convierte la entidad de base de datos a modelo de dominio"""
        from domain import Address
        
        return Address(
            id=self.id,
            client_id=self.client_id,
            address_type=self.address_type,
            street=self.street,
            city=self.city,
            state=self.state,
            postal_code=self.postal_code,
            country=self.country,
            is_default=self.is_default,
            created_at=self.created_at
        )
