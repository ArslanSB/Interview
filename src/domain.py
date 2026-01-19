"""Modelos de dominio - Entidades de negocio puras sin dependencias de infraestructura"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class Address:
    """Modelo de dominio para Address"""
    id: int
    client_id: int
    address_type: str
    street: str
    city: str
    country: str
    state: Optional[str] = None
    postal_code: Optional[str] = None
    is_default: bool = False
    created_at: datetime = None
    
    def get_full_address(self) -> str:
        """Retorna la dirección completa como string"""
        parts = [self.street, self.city]
        if self.state:
            parts.append(self.state)
        if self.postal_code:
            parts.append(self.postal_code)
        parts.append(self.country)
        return ", ".join(parts)
    
    def is_international(self) -> bool:
        """Verifica si la dirección es internacional (no española)"""
        return self.country.lower() not in ['españa', 'spain']


@dataclass
class Client:
    """Modelo de dominio para Client"""
    id: int
    name: str
    email: str
    created_at: datetime
    phone: Optional[str] = None
    addresses: List[Address] = None
    
    def __post_init__(self):
        if self.addresses is None:
            self.addresses = []
    
    def get_default_address(self) -> Optional[Address]:
        """Retorna la dirección por defecto del cliente"""
        for address in self.addresses:
            if address.is_default:
                return address
        return self.addresses[0] if self.addresses else None
    
    def get_addresses_by_type(self, address_type: str) -> List[Address]:
        """Retorna todas las direcciones de un tipo específico"""
        return [addr for addr in self.addresses if addr.address_type == address_type]
    
    def has_international_addresses(self) -> bool:
        """Verifica si el cliente tiene direcciones internacionales"""
        return any(addr.is_international() for addr in self.addresses)
    
    def get_contact_info(self) -> dict:
        """Retorna la información de contacto del cliente"""
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }
