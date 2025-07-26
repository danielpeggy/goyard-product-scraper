#!/usr/bin/env python3
"""
Basic usage example for Goyard Product Scraper
"""

import sys
import os

# Add parent directory to path to import the scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from goyard_scraper_secure import GoyardScraper

def main():
    """
    Example of basic usage
    """
    print("🚀 Goyard Scraper - Basic Usage Example")
    print("=" * 50)
    
    try:
        # Initialize scraper (API key from environment variable)
        scraper = GoyardScraper()
        
        # Extract product metadata for default product
        print("Extracting metadata for default product...")
        product_data = scraper.extract_product_metadata()
        
        if product_data:
            # Display results
            scraper.display_results(product_data)
            
            # Save to custom file
            output_file = scraper.save_results(product_data, "example_output.json")
            print(f"\n💾 Results saved to: {output_file}")
            
            # Access specific fields
            print(f"\n📦 Product Name: {product_data['product_name']}")
            print(f"🎨 Available Colors: {product_data['product_colours']}")
            
        else:
            print("❌ Failed to extract product data")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
