"""
Main Application - Tbilisi Real Estate Management System
Demonstrates the complete functionality of the property management system.
"""

from property import Property, Address, Listing
from property_manager import PropertyManager
from datetime import datetime


def create_sample_properties() -> list:
    """Create sample properties for demonstration."""
    properties = []
    
    # Property 1: Vake Apartment
    address1 = Address(
        street="123 Rustaveli Avenue",
        district="Vake",
        postal_code="0108"
    )
    prop1 = Property(
        property_name="Vake Apartment",
        price_usd=155000,
        is_available=True,
        address=address1,
        bedrooms=2,
        bathrooms=1,
        area_sqm=85.0,
        year_built=2015,
        description="Modern apartment with city views",
        amenities=["Gym", "Parking", "Security", "Balcony"]
    )
    properties.append(prop1)
    
    # Property 2: Saburtalo Penthouse
    address2 = Address(
        street="456 David Agmashenebeli Avenue",
        district="Saburtalo",
        postal_code="0103"
    )
    prop2 = Property(
        property_name="Saburtalo Penthouse",
        price_usd=320000,
        is_available=True,
        address=address2,
        bedrooms=3,
        bathrooms=2,
        area_sqm=150.0,
        year_built=2018,
        description="Luxury penthouse with panoramic views",
        amenities=["Rooftop Terrace", "Smart Home", "Concierge", "Sauna"]
    )
    properties.append(prop2)
    
    # Property 3: Old Town Studio (Sold)
    address3 = Address(
        street="789 Metekhi Street",
        district="Old Town",
        postal_code="0105"
    )
    prop3 = Property(
        property_name="Old Town Studio",
        price_usd=85000,
        is_available=False,  # This property is sold
        address=address3,
        bedrooms=1,
        bathrooms=1,
        area_sqm=45.0,
        year_built=2010,
        description="Cozy studio in historic Old Town",
        amenities=["Balcony", "High Ceilings"]
    )
    properties.append(prop3)
    
    # Property 4: Gldani Family House
    address4 = Address(
        street="321 Nutsubidze Street",
        district="Gldani",
        postal_code="0112"
    )
    prop4 = Property(
        property_name="Gldani Family House",
        price_usd=200000,
        is_available=True,
        address=address4,
        bedrooms=4,
        bathrooms=2,
        area_sqm=180.0,
        year_built=2005,
        description="Spacious family home with garden",
        amenities=["Garden", "Garage", "BBQ Area", "Separate Entrance"]
    )
    properties.append(prop4)
    
    return properties


def create_listings(properties: list) -> list:
    """Create listings with agent information."""
    listings = []
    
    agents = [
        ("Giorgi Beridze", "+995 555 123 456", "giorgi@tbilisiestates.ge"),
        ("Nini Khubashvili", "+995 555 234 567", "nini@tbilisiestates.ge"),
        ("Levan Javakhishvili", "+995 555 345 678", "levan@tbilisiestates.ge"),
        ("Tamara Gogoladze", "+995 555 456 789", "tamara@tbilisiestates.ge"),
    ]
    
    for i, prop in enumerate(properties):
        agent = agents[i % len(agents)]
        listing = Listing(
            property=prop,
            agent_name=agent[0],
            agent_phone=agent[1],
            agent_email=agent[2]
        )
        listings.append(listing)
    
    return listings


def display_welcome_message():
    """Display welcome message."""
    print("\n" + "="*80)
    print(" "*15 + "🏠 TBILISI REAL ESTATE MANAGEMENT SYSTEM 🏠")
    print("="*80 + "\n")


def demonstrate_search_features(manager: PropertyManager):
    """Demonstrate search and filter capabilities."""
    print("\n" + "="*80)
    print("SEARCH DEMONSTRATIONS")
    print("="*80)
    
    # Search by price range
    print("\n📊 Properties between $100,000 - $250,000:")
    results = manager.search_by_price_range(100000, 250000)
    for prop in results:
        print(f"  • {prop.property_name}: ${prop.price_usd:,} - {prop.address.district}")
    
    # Search by bedrooms
    print("\n🛏️  Properties with 2 bedrooms:")
    results = manager.search_by_bedrooms(2)
    for prop in results:
        print(f"  • {prop.property_name}: {prop.bedrooms} beds, {prop.bathrooms} baths")
    
    # Search by district
    print("\n📍 Properties in Vake district:")
    results = manager.search_by_district("Vake")
    for prop in results:
        print(f"  • {prop.property_name}: ${prop.price_usd:,}")
    
    # Get available vs sold
    print(f"\n✅ Available properties: {len(manager.get_available_properties())}")
    print(f"❌ Sold properties: {len(manager.get_sold_properties())}")


def demonstrate_property_details(manager: PropertyManager, listings: list):
    """Display detailed information about properties."""
    print("\n" + "="*80)
    print("PROPERTY DETAILS")
    print("="*80)
    
    for listing in listings[:2]:  # Show first 2 properties
        prop = listing.property
        print(f"\n📋 {prop.property_name}")
        print(f"   Location: {prop.address}")
        print(f"   Price: ${prop.price_usd:,} (${prop.get_price_per_sqm():.2f}/sqm)")
        print(f"   Size: {prop.area_sqm} sqm")
        print(f"   Bedrooms: {prop.bedrooms} | Bathrooms: {prop.bathrooms}")
        print(f"   Built: {prop.year_built}")
        print(f"   Status: {'Available' if prop.is_available else 'Sold'}")
        print(f"   Amenities: {', '.join(prop.amenities)}")
        print(f"   Agent: {listing.agent_name}")
        print(f"   Phone: {listing.agent_phone}")
        print(f"   Days on Market: {listing.get_days_on_market()}")


def main():
    """Main application entry point."""
    display_welcome_message()
    
    # Initialize property manager
    manager = PropertyManager()
    
    # Create and add properties
    print("📦 Loading properties into system...")
    properties = create_sample_properties()
    for prop in properties:
        manager.add_property(prop)
    print(f"✅ Loaded {len(properties)} properties\n")
    
    # Create and add listings
    print("📝 Creating listings with agent information...")
    listings = create_listings(properties)
    for listing in listings:
        manager.add_listing(listing)
    print(f"✅ Created {len(listings)} listings\n")
    
    # Display all properties
    print("📊 ALL PROPERTIES IN INVENTORY:")
    manager.display_all_properties()
    
    # Display statistics
    manager.display_statistics()
    
    # Demonstrate search features
    demonstrate_search_features(manager)
    
    # Show property details
    demonstrate_property_details(manager, listings)
    
    # Demonstrate property status change
    print("\n" + "="*80)
    print("PROPERTY STATUS MANAGEMENT")
    print("="*80)
    prop = manager.get_property_by_name("Vake Apartment")
    if prop:
        print(f"\n🏠 {prop.property_name}")
        print(f"   Before: Available = {prop.is_available}")
        prop.mark_sold()
        print(f"   After mark_sold(): Available = {prop.is_available}")
    
    # Final statistics
    print("\n" + "="*80)
    print("FINAL STATISTICS")
    print("="*80)
    manager.display_statistics()
    
    print("\n✨ Demonstration Complete!\n")


if __name__ == "__main__":
    main()
