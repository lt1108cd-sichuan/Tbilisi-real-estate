"""
Property Management System for Tbilisi Real Estate
This module defines the core data structures for real estate properties.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class Address:
    """Represents a physical address for a property."""
    street: str
    city: str = "Tbilisi"
    district: str = ""
    postal_code: str = ""
    country: str = "Georgia"
    
    def __str__(self) -> str:
        return f"{self.street}, {self.district}, {self.city}, {self.country}"


@dataclass
class Property:
    """Main class representing a real estate property."""
    property_name: str  # 字符串 (String)
    price_usd: int      # 整数 (Integer)
    is_available: bool  # 布尔值 (Boolean)
    address: Address
    bedrooms: int = 0
    bathrooms: int = 0
    area_sqm: float = 0.0
    year_built: Optional[int] = None
    description: str = ""
    amenities: List[str] = None
    created_at: datetime = None
    updated_at: datetime = None
    
    def __post_init__(self):
        """Initialize default values after dataclass initialization."""
        if self.amenities is None:
            self.amenities = []
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
    
    def get_price_per_sqm(self) -> float:
        """Calculate price per square meter."""
        if self.area_sqm > 0:
            return self.price_usd / self.area_sqm
        return 0.0
    
    def mark_sold(self) -> None:
        """Mark property as sold (no longer available)."""
        self.is_available = False
        self.updated_at = datetime.now()
    
    def update_price(self, new_price: int) -> None:
        """Update property price."""
        self.price_usd = new_price
        self.updated_at = datetime.now()
    
    def __str__(self) -> str:
        status = "Available" if self.is_available else "Sold"
        return f"{self.property_name} - ${self.price_usd:,} ({status}) - {self.address}"


@dataclass
class Listing:
    """Represents a real estate listing with agent information."""
    property: Property
    agent_name: str
    agent_phone: str
    agent_email: str
    listing_date: datetime = None
    
    def __post_init__(self):
        """Initialize default values after dataclass initialization."""
        if self.listing_date is None:
            self.listing_date = datetime.now()
    
    def get_days_on_market(self) -> int:
        """Calculate how many days the property has been on market."""
        return (datetime.now() - self.listing_date).days
    
    def __str__(self) -> str:
        return f"Listing: {self.property.property_name} by {self.agent_name}"


# Example usage
if __name__ == "__main__":
    # Create an address
    address = Address(
        street="123 Rustaveli Avenue",
        district="Vake",
        postal_code="0108"
    )
    
    # Create a property
    property_obj = Property(
        property_name="Vake Apartment",
        price_usd=155000,
        is_available=True,
        address=address,
        bedrooms=2,
        bathrooms=1,
        area_sqm=85.0,
        year_built=2015,
        description="Modern apartment with city views",
        amenities=["Gym", "Parking", "Security", "Balcony"]
    )
    
    # Create a listing
    listing = Listing(
        property=property_obj,
        agent_name="Giorgi Beridze",
        agent_phone="+995 555 123 456",
        agent_email="giorgi@tbilisiestates.ge"
    )
    
    # Print information
    print(listing)
    print(f"Price per sqm: ${property_obj.get_price_per_sqm():.2f}")
    print(f"Days on market: {listing.get_days_on_market()}")
