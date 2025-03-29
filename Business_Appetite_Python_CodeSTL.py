# Streamlit version of the Powell Agency Business Appetite Checker
import streamlit as st

# Set up the page
st.set_page_config(page_title="Powell Agency Business Appetite", layout="centered")
st.title("📋 Powell Agency Business Appetite Checker")
st.markdown("Use the dropdowns below to check business eligibility.")

# Full business_appetite dictionary (cut for brevity in this example - include your full version here)
business_appetite = {
    "Artisan Contractors": {
        "Appliance Installation and Repair": {"rating": "Yes", "SIC": "1711", "products": ["BOP", "GL", "WC", "Auto", "UMB"], "notes": ""},
        "Carpentry Work": {"rating": "Kraft Lake", "SIC": "1751", "products": ["Property", "Auto", "UMB"], "notes": ""},
        "Carpet and Upholstery Cleaning": {"rating": "Yes", "SIC": "7217", "products": ["BOP", "GL", "WC", "Auto", "UMB"], "notes": ""},
        "Concrete Work": {"rating": "Kraft Lake", "SIC": "1771", "products": ["Property", "Auto", "UMB"], "notes": "WC is available in CA only"},
        "Drywall, Plastering, Acoustical": {"rating": "Kraft Lake", "SIC": "1742", "products": ["Property", "Auto", "UMB"], "notes": "WC is available in CA only"},
        "Electrical Work": {"rating": "Yes", "SIC": "1731", "products": ["BOP", "GL", "WC", "Auto", "UMB"], "notes": "No alarm or emergency systems; no solar panel installation"},
        "Excavation Work": {"rating": "Kraft Lake", "SIC": "1794", "products": ["Property", "Auto", "UMB"], "notes": ""},
        "Fence Erection": {"rating": "Maybe", "SIC": "1799", "products": ["Property", "Auto", "WC", "UMB"], "notes": "GL not available in CA; no electrified or razor wire fencing"},
        "Floor Covering Installation": {"rating": "Yes", "SIC": "1752", "products": ["BOP", "GL", "WC", "Auto", "UMB"], "notes": "For interior tile or stone, see SIC 1743"},
        "Furniture and Fixture Installation": {"rating": "Yes", "SIC": "1796", "products": ["Property", "Auto", "WC"], "notes": "No cabinet installation"},
        "General Contractors – Industrial": {"rating": "Kraft Lake", "SIC": "1541", "products": ["Property", "Auto", "UMB"], "notes": ""},
        "Greenhouse Erection": {"rating": "Maybe", "SIC": "1799", "products": ["Property", "Auto", "WC", "UMB"], "notes": "GL not available in CA"},
        "Handyman Services": {"rating": "Kraft Lake", "SIC": "1522", "products": ["Property", "Auto", "UMB"], "notes": ""},
        "HVAC": {"rating": "Yes", "SIC": "1711", "products": ["BOP", "GL", "WC", "Auto", "UMB"], "notes": "No boiler work; no solar panel installation; no geothermal work"},
        "Interior Decorators": {"rating": "Yes", "SIC": "7389", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Janitorial Services": {"rating": "Yes", "SIC": "7349", "products": ["BOP", "GL", "WC", "Auto", "UMB"], "notes": "No commercial kitchen degreasing; no exterior"}
    },

    "Auto, Service & Repair": {
    "Antique and Classic Automotive Restoration": {"rating": "Kraft Lake", "SIC": "7532", "products": ["Auto", "WC", "UMB"], "notes": ""},
    "Auto Dealers": {"rating": "Kraft Lake", "SIC": "5511", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Auto Dismantlers": {"rating": "Kraft Lake", "SIC": "5015", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Brake Repair Shops": {"rating": "Yes", "SIC": "7538", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Collision Shops": {"rating": "Yes", "SIC": "7532", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Detail Shops": {"rating": "Yes", "SIC": "7542", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Diesel Engine Repair": {"rating": "Yes", "SIC": "7538", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No heavy truck repair"},
    "Automotive Electrical Repair": {"rating": "Yes", "SIC": "7538", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Emission Testing Shops (without repair)": {"rating": "Yes", "SIC": "7549", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Exhaust Repair Shops": {"rating": "Yes", "SIC": "7533", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Frame Repair Shops": {"rating": "Kraft Lake", "SIC": "7538", "products": ["Auto", "WC", "UMB"], "notes": ""},
    "Automotive Glass Shops": {"rating": "Yes", "SIC": "7536", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Mobile glass repair/replacement is acceptable"},
    "Automotive Oil Change & Lubrication Shops": {"rating": "Yes", "SIC": "7549", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Paint Shops": {"rating": "Yes", "SIC": "7532", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Paint booths must be UL approved"},
    "Automotive Radiator Repair": {"rating": "Yes", "SIC": "7538", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Rustproofing & Undercoating Shops": {"rating": "Yes", "SIC": "7549", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Transmission Repair Shops": {"rating": "Yes", "SIC": "7537", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Upholstery Shops": {"rating": "Yes", "SIC": "7532", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Wheel Alignment Shops": {"rating": "Yes", "SIC": "7538", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Automotive Window Tinting": {"rating": "Yes", "SIC": "7549", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Carwashes": {"rating": "Yes", "SIC": "7542", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Commercial Parking Lots / Garages": {"rating": "Kraft Lake", "SIC": "7521", "products": ["Auto", "WC", "UMB"], "notes": ""},
    "General Automotive Repair": {"rating": "Yes", "SIC": "7538", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""}
    },

    "Habitational": {
        "Apartments": {"rating": "Yes", "SIC": "6513", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Condominiums & Townhomes": {"rating": "Yes", "SIC": "8641", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "PrefCAM coverage is available"},
        "Dwellings (1-4 Unit)": {"rating": "Maybe", "SIC": "6514", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Risks owned by individuals or trusts must be"},
        "HOAs / PUDs": {"rating": "Maybe", "SIC": "8699", "products": ["WC"], "notes": "PrefCAM coverage is available"},
        "Individual Condo Units Leased to Others": {"rating": "Yes", "SIC": "6514", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Must be placed through Personal Lines"}
            
    },

    "Real Estate": {
        "Churches": {"rating": "Kraft Lake", "SIC": "6512", "products": ["Auto", "WC"], "notes": ""},
        "Commercial Condo Associations": {"rating": "Yes", "SIC": "6512", "products": ["BOP", "Auto", "WC"], "notes": "Condominium Association Coverage and Directors & Officers Liability coverage is available"},
        "Commercial Parking Lots / Garages": {"rating": "Kraft Lake", "SIC": "7521", "products": ["Auto", "WC"], "notes": ""},
        "Schools": {"rating": "Kraft Lake", "SIC": "6512", "products": ["Auto"], "notes": ""},
        "Self-Storage Facilities": {"rating": "Yes", "SIC": "6512", "products": ["BOP", "WC"], "notes": "Customer Property-Legal Liability and Sale and Disposal Liability apply to this class"},
        "Theaters": {"rating": "Kraft Lake", "SIC": "6512", "products": ["Auto"], "notes": ""},
        "Warehouses": {"rating": "Yes", "SIC": "6512", "products": ["BOP", "WC"], "notes": ""}
    },

    "Manufacturing": {
        "Computer & Office Equipment": {
            "Calculating and Accounting Equipment": {"rating": "Maybe", "SIC": "3578", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Computer Manufacturing": {"rating": "Kraft Lake", "SIC": "3571", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
            "Office Machines, NOC": {"rating": "Maybe", "SIC": "3579", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"}
        },
        "Electrical Equipment & Appliances": {
            "Household Appliances, NOC": {"rating": "Maybe", "SIC": "3639", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Household Audio and Video Equipment": {"rating": "Maybe", "SIC": "3651", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Household Cooking Equipment": {"rating": "Maybe", "SIC": "3631", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Housewares, Small Appliances": {"rating": "Maybe", "SIC": "3634", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Intercom Systems and Equipment": {"rating": "Maybe", "SIC": "3669", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed; no security, fire, or burglar alarm equipment"},
            "Laundry Equipment – Household": {"rating": "Maybe", "SIC": "3633", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Magnetic and Optical Recording Media": {"rating": "Maybe", "SIC": "3695", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Radio and Television Communication Equipment": {"rating": "Maybe", "SIC": "3663", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed; no global positioning satellite equipment, components or accessories"},
            "Records and Pre-Recorded Audio Tapes and Disks": {"rating": "Maybe", "SIC": "3652", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Refrigeration Equipment Mfg. – Household": {"rating": "Maybe", "SIC": "3632", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed"},
            "Telephone and Telegraph Equipment": {"rating": "Maybe", "SIC": "3661", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed; no cell phones or computer modems"},
            "Vacuum Cleaners": {"rating": "Maybe", "SIC": "3635", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Products must be UL listed; no commercial or industrial vacuums or sweepers"}
    },


    "Restaurants": {
        "Bagel / Doughnut Shops (Retail)": {"rating": "Yes", "SIC": "5461", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "See SIC 5812A If grilling or frying"},
        "Banquet Halls": {"rating": "Kraft Lake", "SIC": "9999", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Bars, Taverns, Pubs, & Nightclubs": {"rating": "Kraft Lake", "SIC": "9999", "products": ["Auto", "UMB"], "notes": ""},
        "Buffets": {"rating": "Yes", "SIC": "5812B", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Cafeterias": {"rating": "Kraft Lake", "SIC": "9999", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Coffee Shops / Juice Bars (Retail)": {"rating": "Yes", "SIC": "5499", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "See SIC 5812A If grilling or frying"},
        "Dinner Theaters": {"rating": "Kraft Lake", "SIC": "9999", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Drive-Ins": {"rating": "Yes", "SIC": "5812A", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Fast Food": {"rating": "Yes", "SIC": "5812A", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Fine Dining": {"rating": "Yes", "SIC": "5812D", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Full Service Casual Dining": {"rating": "Yes", "SIC": "5812B", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Ice Cream Parlors (Retail)": {"rating": "Yes", "SIC": "5451", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "See SIC 5812A If grilling or frying"},
        "Mobile Food Vendors / Food Trucks": {"rating": "Kraft Lake", "SIC": "9999", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Pizza Parlors": {"rating": "Yes", "SIC": "5812E", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "See SIC 5812A If grilling or frying"},
        "Sandwich Shops / Delis": {"rating": "Yes", "SIC": "5812E", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "See SIC 5812A If grilling or frying"}
    },
  "Food Processors": {
        "Bottled and Canned Soft Drinks and Carbonated Waters": {"rating": "Maybe", "SIC": "2086", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No energy drinks or non-pasteurized drinks; no baby foods or juices"},
        "Bread and Bakery Plants": {"rating": "Maybe", "SIC": "2051", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No operations that have dust exposures such as flour or grain milling, cake mix, spice or tea manufacturing"},
        "Candy and Other Confectionery Products": {"rating": "Maybe", "SIC": "2064", "products": ["WC", "UMB"], "notes": ""},
        "Cereal Breakfast Foods": {"rating": "Maybe", "SIC": "2043", "products": ["WC", "UMB"], "notes": "No baby foods or herbal supplements"},
        "Cheese and Other Dairy Products": {"rating": "Kraft Lake", "SIC": "2022", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Chewing Gum": {"rating": "Maybe", "SIC": "2067", "products": ["BOP", "UMB"], "notes": ""},
        "Chocolate and Cocoa Products": {"rating": "Maybe", "SIC": "2066", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Cookies, Crackers and Pretzels": {"rating": "Maybe", "SIC": "2052", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No baby foods or juices"},
        "Flavorings, Food Colors, Extracts and Syrups": {"rating": "Maybe", "SIC": "2087", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No baby foods or juices"},
        "Frozen Bakery Products": {"rating": "Maybe", "SIC": "2053", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Malt Beverages": {"rating": "Maybe", "SIC": "2082", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Manufactured Ice": {"rating": "Maybe", "SIC": "2097", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No dry ice manufacturing"},
        "Micro-Breweries": {"rating": "Maybe", "SIC": "2083", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No liquor or wine manufacturing"},
        "Pasta and Noodles": {"rating": "Maybe", "SIC": "2098", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No baby foods or juices"},
        "Potato Chips and Similar Snacks": {"rating": "Kraft Lake", "SIC": "2096", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Roasted Coffee": {"rating": "Kraft Lake", "SIC": "2095", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Sausages and Prepared Meat Products": {"rating": "Kraft Lake", "SIC": "2013", "products": ["Auto", "WC", "UMB"], "notes": ""}
    },

    "Luggage and Personal Leather Goods": {
        "Luggage, Leather, Canvas and Nylon": {"rating": "Maybe", "SIC": "3161", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Personal Leather Goods": {"rating": "Maybe", "SIC": "3172", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Women's Handbags and Purses": {"rating": "Maybe", "SIC": "3171", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""}
    },

    "Metal Working & Metal Products Fabricators": {
        "Air Conditioning Equipment": {"rating": "Maybe", "SIC": "3585", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Architectural and Ornamental Metal Products": {"rating": "Maybe", "SIC": "3446", "products": ["BOP", "Auto", "UMB"], "notes": "No structural products or components"},
        "Automotive Stamping": {"rating": "Maybe", "SIC": "3465", "products": ["BOP", "Auto", "UMB"], "notes": ""},
        "Bolts, Nuts, Screws, Rivets": {"rating": "Maybe", "SIC": "3452", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Cold Metal Stamping": {"rating": "Maybe", "SIC": "3469", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Cutlery and Flatware": {"rating": "Maybe", "SIC": "3421", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Cutting Tools and Machine Tools": {"rating": "Maybe", "SIC": "3545", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Die Casting – Nonferrous Metals": {"rating": "Maybe", "SIC": "3364", "products": ["BOP", "WC", "UMB"], "notes": "No beryllium, copper, lead, magnesium, mercury, titanium, or zinc die-casting"},
        "Drapery Hardware, Window Blinds and Shades": {"rating": "Maybe", "SIC": "2591", "products": ["WC", "UMB"], "notes": ""},
        "Electroplating, Plating, Polishing, Anodizing": {"rating": "Kraft Lake", "SIC": "3471", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Fabricated Pipe and Pipe Fittings": {"rating": "Maybe", "SIC": "3498", "products": ["BOP", "Auto", "UMB"], "notes": ""},
        "Fabricated Wire Products": {"rating": "Maybe", "SIC": "3496", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
        "Fasteners, Buttons, Needles and Pins": {"rating": "Maybe", "SIC": "3965", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""}
    },


    "Retail, Office & Service": {
    "Coin-Operated Laundries": {"rating": "Yes", "SIC": "7215", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Diaper Service": {"rating": "Yes", "SIC": "7219", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Dry Cleaning Plants (Except Rug)": {"rating": "Yes", "SIC": "7216", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Garment Pressing and Cleaner's Agents": {"rating": "Yes", "SIC": "7212", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Tailors, Garment Alteration Shops": {"rating": "Yes", "SIC": "7219", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Uniform and Linen Supply": {"rating": "Yes", "SIC": "7213", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Bakeries, Bagels, Doughnuts, Pretzel Stores": {"rating": "Yes", "SIC": "5461", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "See Restaurant Industry If grilling or frying"},
    "Candy, Confectionery, Nut and Popcorn Stores": {"rating": "Yes", "SIC": "5441", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Coffee Shops": {"rating": "Yes", "SIC": "5499", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "See Restaurant Industry If grilling or frying"},
    "Convenience Stores": {"rating": "Maybe", "SIC": "5411", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Stores over 10,000 sq. ft. are ineligible; no check cashing or money wire transfer services"},
    "Fruit, Produce and Vegetable Markets or Stands": {"rating": "Yes", "SIC": "5431", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Gas Stations with or without Convenience Stores": {"rating": "Maybe", "SIC": "5411", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Stores over 10,000 sq. ft. are ineligible; no check cashing or money wire transfer services; no auto repair services"},
    "Grocery Stores": {"rating": "Maybe", "SIC": "5411", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Stores over 10,000 sq. ft. are ineligible; no check cashing or money wire transfer services"},
    "Ice Cream, Frozen Yogurt, Custard Shops": {"rating": "Yes", "SIC": "5451", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Juice Bars": {"rating": "Yes", "SIC": "5499", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "See Restaurant  Industry If grilling or frying"},
    "Liquor Stores": {"rating": "Maybe", "SIC": "5921", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "Not eligible in Alabama and Michigan; additional requirements apply to this class"},
    "Meat, Fish, Seafood Markets": {"rating": "Yes", "SIC": "5421", "products": ["BOP", "Auto", "WC", "UMB"], "notes": "No slaughtering or wild game processing"},
    "Specialty Food Stores": {"rating": "Yes", "SIC": "5499", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Tobacco, Marijuana, Vape Stores": {"rating": "Kraft Lake", "SIC": "5411", "products": ["BOP", "Auto", "WC", "UMB"], "notes": ""},
    "Vitamin and Health Supplement Stores": {"rating": "Kraft Lake", "SIC": "5499", "products": ["Auto", "WC"], "notes": ""}
},
    

"Wholesale Distributors": {
        "Commercial Equipment, Not Elsewhere Classified": {"rating": "Maybe", "SIC": "5046", "products": ["Auto", "WC", "UMB"], "notes": "No fire suppression equipment and kitchen hoods"},
        "Electrical Equipment, Wiring and Construction Materials": {"rating": "Maybe", "SIC": "5063", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Electronic Parts and Equipment, Not Elsewhere Classified": {"rating": "Maybe", "SIC": "5065", "products": ["Auto", "WC", "UMB"], "notes": "No computers or computer-related equipment"},
        "Farm and Garden Machinery and Equipment": {"rating": "Maybe", "SIC": "5083", "products": ["Auto", "UMB"], "notes": ""},
        "Furniture": {"rating": "Maybe", "SIC": "5021", "products": ["Auto", "WC", "UMB"], "notes": "No antique or used merchandise"},
        "Hardware": {"rating": "Maybe", "SIC": "5072", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Heating/Air Conditioning Equipment and Supplies": {"rating": "Maybe", "SIC": "5075", "products": ["Auto", "WC", "UMB"], "notes": "No space heaters"},
        "House Furnishings": {"rating": "Maybe", "SIC": "5023", "products": ["Auto", "WC", "UMB"], "notes": "No Persian or Oriental rugs"},
        "Industrial and Personal Service Paper": {"rating": "Maybe", "SIC": "5113", "products": ["Auto", "WC", "UMB"], "notes": "Fire suppression system and central reporting fire alarm required for total property limits over 500,000"},
        "Lumber, Plywood, Millwork, and Wood Panels": {"rating": "Kraft Lake", "SIC": "5031", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Motor Vehicles Supplies and New Parts": {"rating": "Maybe", "SIC": "5013", "products": ["Auto", "WC", "UMB"], "notes": "No batteries, air bags or seat belts"},
        "Office Equipment": {"rating": "Maybe", "SIC": "5044", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Ophthalmic Goods": {"rating": "Maybe", "SIC": "5048", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Photographic Equipment and Supplies": {"rating": "Maybe", "SIC": "5043", "products": ["Auto", "WC", "UMB"], "notes": "No equipment rental"},
        "Plumbing and Heating Equipment and Supplies": {"rating": "Maybe", "SIC": "5074", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Printing and Writing Paper": {"rating": "Maybe", "SIC": "5111", "products": ["Auto", "WC", "UMB"], "notes": "Fire suppression system and central reporting fire alarm required"},
        "Refrigeration Equipment and Supplies": {"rating": "Maybe", "SIC": "5078", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Service Establishment Equipment and Supplies": {"rating": "Maybe", "SIC": "5087", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Stationery and Office Supplies": {"rating": "Maybe", "SIC": "5112", "products": ["Auto", "WC", "UMB"], "notes": "Fire suppression system and central reporting fire alarm required for total property limits over 500,000"},
        "Toys and Hobby Goods and Supplies": {"rating": "Kraft Lake", "SIC": "5092", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Beer and Ale": {"rating": "Maybe", "SIC": "5181", "products": ["Auto", "WC", "UMB"], "notes": "No bottling operations"},
        "Confectionary": {"rating": "Maybe", "SIC": "5145", "products": ["Auto", "WC", "UMB"], "notes": "No bottling operations"},
        "Fresh Fruits and Vegetables": {"rating": "Kraft Lake", "SIC": "5148", "products": ["WC", "UMB"], "notes": ""},
        "Grain and Field Beans": {"rating": "Maybe", "SIC": "5153", "products": ["Auto", "WC", "UMB"], "notes": "No grain processing or farming operations"},
        "Meats and Meat Products": {"rating": "Kraft Lake", "SIC": "5147", "products": ["WC", "UMB"], "notes": ""},
        "Wine and Distilled Alcoholic Beverages": {"rating": "Maybe", "SIC": "5182", "products": ["Auto", "WC", "UMB"], "notes": "No bottling operations"},
        "Books, Periodicals and Newspapers": {"rating": "Maybe", "SIC": "5192", "products": ["Auto", "WC", "UMB"], "notes": ""},
        "Flowers, Nursery Stock and Florist's Supplies": {"rating": "Yes", "SIC": "5193", "products": ["Auto", "WC"], "notes": ""},
        "Jewelry, Watches, Precious Stones and Precious Metals": {"rating": "Kraft Lake", "SIC": "5094", "products": [], "notes": ""},
        "Piece Goods, Notions and Other Dry Goods": {"rating": "Kraft Lake", "SIC": "5131", "products": [], "notes": ""}
},

"Workers’ Compensation": {
    "General Workers": {"rating": "Yes", "SIC": "0000", "products": ["WC"], "notes": "Requires workplace safety audits."},
    "Healthcare Workers": {"rating": "Yes", "SIC": "8011", "products": ["WC"], "notes": "Requires malpractice insurance."}
},
}
}

# User selects business type and subcategory
business_type = st.selectbox("Select Business Type:", options=list(business_appetite.keys()))
subcategory_list = list(business_appetite[business_type].keys())
subcategory = st.selectbox("Select Subcategory:", options=subcategory_list)

# Display results
if st.button("Check Eligibility"):
    data = business_appetite[business_type][subcategory]
    st.markdown(f"### 📌 {subcategory}")
    st.markdown(f"**✅ Approval Status:** {data.get('rating')}")
    st.markdown(f"**📊 SIC Code:** {data.get('SIC')}")
    st.markdown(f"**📦 Products:** {', '.join(data.get('products', []) if data.get('products') else [])}")
    st.markdown(f"**📝 Notes:** {data.get('notes') if data.get('notes') else 'None'}")

# Footer
st.markdown("---")
st.markdown("© 2025 Powell Agency | Built by Keith Coleman Jr")
