````markdown name=README.md
# 🏠 Tbilisi Real Estate Management System

A comprehensive Python application for managing real estate properties in Tbilisi, Georgia.

## 📋 Features

- **Property Management**: Create and manage property listings with detailed information
- **Search Capabilities**: Search properties by price range, bedrooms, district, and more
- **Agent Information**: Track real estate agents and their listings
- **Statistics**: Get insights into your property inventory
- **Price Analysis**: Calculate price per square meter and other metrics
- **Status Tracking**: Mark properties as available or sold

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/lt1108cd-sichuan/Tbilisi-real-estate.git
cd Tbilisi-real-estate
```

2. Install dependencies (optional):
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## 📚 Usage Examples

### Create a Property

```python
from property import Property, Address

address = Address(
    street="123 Main Street",
    district="Vake",
    postal_code="0108"
)

property_obj = Property(
    property_name="Vake Apartment",
    price_usd=155000,
    is_available=True,
    address=address,
    bedrooms=2,
    bathrooms=1,
    area_sqm=85.0,
    amenities=["Gym", "Parking"]
)
```

### Use the Property Manager

```python
from property_manager import PropertyManager

manager = PropertyManager()
manager.add_property(property_obj)

# Search by price range
results = manager.search_by_price_range(100000, 200000)

# Search by district
results = manager.search_by_district("Vake")

# Get statistics
print(f"Average Price: ${manager.get_average_price():,.2f}")
print(f"Total Inventory: ${manager.get_total_inventory_value():,}")
```

### Create a Listing with Agent Info

```python
from property import Listing

listing = Listing(
    property=property_obj,
    agent_name="Giorgi Beridze",
    agent_phone="+995 555 123 456",
    agent_email="giorgi@tbilisiestates.ge"
)
```

## 📁 Project Structure

```
Tbilisi-real-estate/
├── property.py           # Core data structures (Property, Address, Listing)
├── property_manager.py   # Property management and search functionality
├── main.py              # Main application with demonstrations
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 🔧 API Reference

### Property Class

- `get_price_per_sqm()` - Calculate price per square meter
- `mark_sold()` - Mark property as sold
- `update_price(new_price)` - Update property price

### PropertyManager Class

**Search Methods:**
- `search_by_price_range(min, max)` - Find properties in price range
- `search_by_bedrooms(count)` - Find properties by bedroom count
- `search_by_district(name)` - Find properties in specific district
- `get_property_by_name(name)` - Find property by name

**Statistics Methods:**
- `get_average_price()` - Calculate average price
- `get_total_inventory_value()` - Total value of all properties
- `get_cheapest_property()` - Find cheapest available property
- `get_most_expensive_property()` - Find most expensive property
- `get_largest_property()` - Find largest property

**Management Methods:**
- `add_property(property)` - Add property to inventory
- `add_listing(listing)` - Add property listing
- `get_available_properties()` - Get all available properties
- `get_sold_properties()` - Get all sold properties
- `display_all_properties()` - Display formatted property list
- `display_statistics()` - Display inventory statistics

## 📊 Data Types

The system demonstrates Python data types:

```python
property_name = "Vake Apartment"  # 字符串 (String)
price_usd = 155000               # 整数 (Integer)
is_available = True              # 布尔值 (Boolean)
area_sqm = 85.0                  # 浮点数 (Float)
amenities = ["Gym", "Parking"]   # 列表 (List)
address = Address(...)           # 对象 (Object)
```

## 🚀 Future Enhancements

- Database integration (SQLite/PostgreSQL)
- Web interface with Flask
- Data visualization with matplotlib
- Export to CSV/PDF
- Email notifications
- API for mobile apps

## 📝 License

This project is open source and available under the MIT License.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For support, email: lt1108cd@gmail.com

---

**Created by**: lt1108cd-sichuan  
**Last Updated**: 2026-05-06
````
