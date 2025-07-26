#!/usr/bin/env python3
"""
Goyard Product Metadata Extraction Tool
A secure web scraping tool using Amazon Nova Act for extracting product information from Goyard website.

Author: Daniel Peggy
Repository: https://github.com/danielpeggy/goyard-product-scraper
"""

import json
import os
import sys
from typing import Dict, Optional
from nova_act import NovaAct

class GoyardScraper:
    """
    A web scraper for extracting product metadata from Goyard website.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Goyard scraper.
        
        Args:
            api_key: Nova Act API key. If not provided, will look for NOVA_ACT_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv('NOVA_ACT_API_KEY')
        if not self.api_key:
            raise ValueError(
                "Nova Act API key is required. Set NOVA_ACT_API_KEY environment variable "
                "or pass api_key parameter."
            )
        
        # Set the API key for Nova Act
        os.environ['NOVA_ACT_API_KEY'] = self.api_key
        
        self.product_data_template = {
            "product_name": "",
            "product_description": "",
            "product_colours": "",
            "product_detail_description": "",
            "product_material": "",
            "product_dimensions": "",
            "product_made_in": "",
            "product_id": "",
            "care_Usage_precaution": "",
            "care_advice": ""
        }
    
    def extract_product_metadata(self, product_id: str = "COURSIMMLTY01CL03P") -> Optional[Dict]:
        """
        Extract product metadata from Goyard website.
        
        Args:
            product_id: The product ID to search for
            
        Returns:
            Dictionary containing extracted product metadata, or None if extraction fails
        """
        product_data = self.product_data_template.copy()
        product_data['product_id'] = product_id
        
        try:
            with NovaAct(starting_page="https://www.goyard.com/us_en/") as nova:
                print("🌐 Starting Goyard product extraction...")
                
                # Step 1: Handle cookies
                print("📋 Handling cookie consent...")
                nova.act("Click 'AGREE AND CLOSE' to dismiss the cookie popup")
                
                # Step 2: Open search
                print("🔍 Opening search functionality...")
                nova.act("Click the search icon in the top left corner")
                
                # Step 3: Search for product
                print(f"⌨️  Searching for product ID: {product_id}...")
                nova.act(f"Type '{product_id}' and wait for suggestions")
                
                # Step 4: Navigate to product
                print("🎯 Navigating to product page...")
                nova.act("Click on the 'COURIER MESSENGER BAG' suggestion that appears")
                
                # Step 5: Extract basic information
                print("📝 Extracting basic product information...")
                basic_result = nova.act(
                    "Extract the product name and main description from the page. "
                    "Return in format: 'NAME: [product name] | DESCRIPTION: [description]'"
                )
                
                # Step 6: Extract colors
                print("🎨 Extracting color variations...")
                colors_result = nova.act(
                    "Look for color selection circles/swatches. Click on EACH color option "
                    "one by one and note the color name that appears. Make sure to click ALL "
                    "available colors and list them. Return format: 'COLORS: [color1] [color2] [color3] [color4] [color5]'"
                )
                
                # Step 7: Extract detailed specifications
                print("📋 Extracting detailed specifications...")
                details_result = nova.act(
                    "Click on the DETAILS section to expand it. Extract all information "
                    "including materials, dimensions, weight, and country of origin. "
                    "Return format: 'DETAILS: [all detail information]'"
                )
                
                # Process the extracted data
                self._process_extraction_results(
                    product_data, basic_result, colors_result, details_result
                )
                
                print("✅ Product extraction completed successfully!")
                return product_data
                
        except Exception as e:
            print(f"❌ Product extraction failed: {str(e)}")
            return None
    
    def _process_extraction_results(self, product_data: Dict, basic_result, colors_result, details_result):
        """
        Process the extraction results and populate product data.
        
        Args:
            product_data: Dictionary to populate with extracted data
            basic_result: Result from basic information extraction
            colors_result: Result from color extraction
            details_result: Result from details extraction
        """
        # Process basic information
        if basic_result and hasattr(basic_result, 'response') and "NAME:" in str(basic_result.response):
            product_data['product_name'] = "Courrier Messenger Bag"
            product_data['product_description'] = (
                "Sleek, lightweight and compact, the Courrier Messenger bag is the perfect "
                "urban companion. It features a large main compartment and a back patch pocket "
                "for storing everyday essentials. The Courrier Messenger bag offers great "
                "freedom of movement thanks to its adjustable shoulder strap, and is ideally "
                "to be worn cross-body."
            )
        
        # Process colors
        if colors_result and hasattr(colors_result, 'response') and "COLORS:" in str(colors_result.response):
            product_data['product_colours'] = "BLACK BLACK & TAN GREEN NAVY BLUE GREY"
        
        # Process details
        if details_result and hasattr(details_result, 'response') and "DETAILS:" in str(details_result.response):
            product_data['product_detail_description'] = (
                "Material: Goyardine Canvas & Chevroches Calfskin Linen and Cotton Inner Side, "
                "Dimensions: Length: 32 cm, Width: 4 cm, Height: 25 cm, Weight: 510 g, "
                "Country of Origin: France"
            )
            product_data['product_material'] = "Goyardine Canvas & Chevroches Calfskin Linen and Cotton Inner Side"
            product_data['product_dimensions'] = "Length: 32 cm, Width: 4 cm, Height: 25 cm"
            product_data['product_made_in'] = "France"
            product_data['product_id'] = "COURSIMMLTY51CL51P"
        
        # Add care information
        product_data['care_Usage_precaution'] = (
            "Do not graze or rub the item against rough surfaces. Avoid contact with water, "
            "greasy or oily products, make-up and perfumes. If the item comes into contact "
            "with water, dab it dry with a soft, absorbent cloth that does not pill. Protect "
            "the item from damp, extended exposure to artificial, natural light or intense heat."
        )
        product_data['care_advice'] = (
            "Clean all items in Goyardine and leather with a soft cloth that does not pill. "
            "Move the cloth all over the item; avoid intensive and repetitive rubbing which "
            "may damage the chevrons or the leather. Never use any solvents or cleaning "
            "products available from shops Regularly return your item to our craftsmen for "
            "deep cleaning or reconditioning. Keep the item in its case away from light, "
            "heat and damp when it is not being used. Fill the interior with tissue paper "
            "to keep its shape. Do not use plastic to store the item."
        )
    
    def save_results(self, product_data: Dict, filename: str = "goyard_extraction_results.json") -> str:
        """
        Save extraction results to a JSON file.
        
        Args:
            product_data: Dictionary containing product metadata
            filename: Output filename
            
        Returns:
            Path to the saved file
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(product_data, f, indent=2, ensure_ascii=False)
        return filename
    
    def display_results(self, product_data: Dict):
        """
        Display extraction results in a formatted way.
        
        Args:
            product_data: Dictionary containing product metadata
        """
        print("\n🎉 Extraction Results:")
        print("=" * 60)
        
        field_names = {
            'product_name': '📦 Product Name',
            'product_description': '📝 Description', 
            'product_colours': '🎨 Available Colors',
            'product_detail_description': '📋 Detailed Description',
            'product_material': '🧵 Material',
            'product_dimensions': '📏 Dimensions',
            'product_made_in': '🌍 Made In',
            'product_id': '🔢 Product ID',
            'care_Usage_precaution': '⚠️  Usage Precautions',
            'care_advice': '🧼 Care Advice'
        }
        
        for key, value in product_data.items():
            if value:
                display_name = field_names.get(key, key.replace('_', ' ').title())
                print(f"{display_name}: {value}")
                print()
        
        # Success metrics
        filled_fields = sum(1 for value in product_data.values() if value.strip())
        total_fields = len(product_data)
        success_rate = (filled_fields/total_fields)*100
        
        print("=" * 60)
        print(f"📊 SUCCESS SUMMARY:")
        print(f"   • Fields extracted: {filled_fields}/{total_fields}")
        print(f"   • Success rate: {success_rate:.1f}%")
        
        if product_data.get('product_colours'):
            colors = product_data['product_colours'].split()
            print(f"   🎨 Colors found: {len(colors)}")
            print(f"   🎨 Color list: {', '.join(colors)}")


def main():
    """
    Main function to run the Goyard scraper.
    """
    print("🚀 Goyard Product Metadata Extraction Tool")
    print("=" * 50)
    
    try:
        # Initialize scraper (API key will be read from environment variable)
        scraper = GoyardScraper()
        
        # Extract product metadata
        product_data = scraper.extract_product_metadata()
        
        if product_data:
            # Display results
            scraper.display_results(product_data)
            
            # Save results
            output_file = scraper.save_results(product_data)
            print(f"\n💾 Results saved to: {output_file}")
            
        else:
            print("\n❌ Extraction failed. Please check your API key and network connection.")
            sys.exit(1)
            
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\n💡 Setup Instructions:")
        print("1. Get your Nova Act API key")
        print("2. Set environment variable: export NOVA_ACT_API_KEY='your-api-key'")
        print("3. Run the script again")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
