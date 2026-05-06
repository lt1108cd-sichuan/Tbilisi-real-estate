"""
Property Manager Module
Manages collections of properties and provides search/analytics functionality.
"""

from typing import List, Optional
from property import Property, Listing


class PropertyManager:
    """Manages real estate properties and provides search capabilities."""
    
    def __init__(self):
        """Initialize the property manager."""
        self.properties: List[Property] = []
        self.listings: List[Listing] = []
    
    def add_property(self, property: Property) -> None:
        """Add a property to the inventory."""
        self.properties.append(property)
    
    def add_listing(self, listing: Listing) -> None:
        """Add a listing with agent information."""
        self.listings.append(listing)
    
    def get_property_by_name(self, name: str) -> Optional[Property]:
        """Find a property by name."""
        for prop in self.properties:
            if prop.property_name.lower() == name.lower():
                return prop
        return None
    
    def search_by_price_range(self, min_price: int, max_price: int) -> List[Property]:
        """Search for properties within a price range."""
        return [
            prop for prop in self.properties
            if min_price <= prop.price_usd <= max_price
        ]
    
    def search_by_bedrooms(self, bedroom_count: int) -> List[Property]:
        """Search for properties with a specific number of bedrooms."""
        return [
            prop for prop in self.properties
            if prop.bedrooms == bedroom_count
        ]
    
    def search_by_district(self, district: str) -> List[Property]:
        """Search for properties in a specific district."""
        return [
            prop for prop in self.properties
            if prop.address.district.lower() == district.lower()
        ]
    
    def search_by_name(self, name_substring: str) -> List[Property]:
        """Search for properties by name substring."""
        return [
            prop for prop in self.properties
            if name_substring.lower() in prop.property_name.lower()
        ]
    
    def get_available_properties(self) -> List[Property]:
        """Get all available properties."""
        return [prop for prop in self.properties if prop.is_available]
    
    def get_sold_properties(self) -> List[Property]:
        """Get all sold properties."""
        return [prop for prop in self.properties if not prop.is_available]
    
    def get_properties_by_size(self, min_sqm: float = 0, max_sqm: float = float('inf')) -> List[Property]:
        """Get properties within a size range."""
        return [
            prop for prop in self.properties
            if min_sqm <= prop.area_sqm <= max_sqm
        ]
    
    def get_average_price(self) -> float:
        """Calculate the average price of all properties."""
        if not self.properties:
            return 0.0
        return sum(prop.price_usd for prop in self.properties) / len(self.properties)
    
    def get_total_inventory_value(self) -> int:
        """Calculate total value of all properties."""
        return sum(prop.price_usd for prop in self.properties)
    
    def get_average_price_available(self) -> float:
        """Calculate average price of available properties."""
        available = self.get_available_properties()
        if not available:
            return 0.0
        return sum(prop.price_usd for prop in available) / len(available)
    
    def get_cheapest_property(self) -> Optional[Property]:
        """Find the cheapest available property."""
        available = self.get_available_properties()
        return min(available, key=lambda p: p.price_usd) if available else None
    
    def get_most_expensive_property(self) -> Optional[Property]:
        """Find the most expensive available property."""
        available = self.get_available_properties()
        return max(available, key=lambda p: p.price_usd) if available else None
    
    def get_largest_property(self) -> Optional[Property]:
        """Find the largest property by area."""
        return max(self.properties, key=lambda p: p.area_sqm) if self.properties else None
    
    def get_smallest_property(self) -> Optional[Property]:
        """Find the smallest property by area."""
        return min(self.properties, key=lambda p: p.area_sqm) if self.properties else None
    
    def get_best_price_per_sqm(self) -> Optional[Property]:
        """Find property with best price per square meter."""
        available = self.get_available_properties()
        if not available:
            return None
        return min(available, key=lambda p: p.get_price_per_sqm())
    
    def get_properties_count(self) -> int:
        """Get total number of properties."""
        return len(self.properties)
    
    def get_available_count(self) -> int:
        """Get count of available properties."""
        return len(self.get_available_properties())
    
    def get_sold_count(self) -> int:
        """Get count of sold properties."""
        return len(self.get_sold_properties())
    
    def display_all_properties(self) -> None:
        """Display all properties in a formatted table."""
        if not self.properties:
            print("No properties in inventory.")
            return
        
        print("\n" + "-" * 120)
        print(f"{'Property Name':<25} {'Location':<20} {'Price':>12} {'Size':>8} {'Beds':<5} {'Status':<10}")
        print("-" * 120)
        
        for prop in self.properties:
            status = "Available" if prop.is_available else "Sold"
            print(f"{prop.property_name:<25} {prop.address.district:<20} ${prop.price_usd:>11,} {prop.area_sqm:>7.0f}m² {prop.bedrooms:<5} {status:<10}")
        
        print("-" * 120)
    
    def display_statistics(self) -> None:
        """Display inventory statistics."""
        print("\n" + "="*80)
        print("📈 INVENTORY STATISTICS")
        print("="*80)
        
        print(f"\n📊 Property Count:")
        print(f"   Total Properties: {self.get_properties_count()}")
        print(f"   Available: {self.get_available_count()}")
        print(f"   Sold: {self.get_sold_count()}")
        
        if self.properties:
            print(f"\n💰 Price Statistics:")
            print(f"   Total Inventory Value: ${self.get_total_inventory_value():,}")
            print(f"   Average Price (All): ${self.get_average_price():,.2f}")
            print(f"   Average Price (Available): ${self.get_average_price_available():,.2f}")
            
            cheapest = self.get_cheapest_property()
            if cheapest:
                print(f"   Cheapest: {cheapest.property_name} - ${cheapest.price_usd:,}")
            
            most_expensive = self.get_most_expensive_property()
            if most_expensive:
                print(f"   Most Expensive: {most_expensive.property_name} - ${most_expensive.price_usd:,}")
            
            print(f"\n📐 Size Statistics:")
            largest = self.get_largest_property()
            if largest:
                print(f"   Largest: {largest.property_name} - {largest.area_sqm:.0f} sqm")
            
            smallest = self.get_smallest_property()
            if smallest:
                print(f"   Smallest: {smallest.property_name} - {smallest.area_sqm:.0f} sqm")
            
            best_value = self.get_best_price_per_sqm()
            if best_value:
                print(f"   Best Value: {best_value.property_name} - ${best_value.get_price_per_sqm():.2f}/sqm")
        
        print()


# Example usage
if __name__ == "__main__":
    from property import Address
    
    # Create manager
    manager = PropertyManager()
    
    # Create and add a sample property
    address = Address(
        street="123 Main Street",
        district="Vake",
        postal_code="0108"
    )
    
    prop = Property(
        property_name="Sample Apartment",
        price_usd=150000,
        is_available=True,
        address=address,
        bedrooms=2,
        bathrooms=1,
        area_sqm=80.0
    )
    
    manager.add_property(prop)
    manager.display_all_properties()
    manager.display_statistics()
