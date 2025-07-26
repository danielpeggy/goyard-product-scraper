# Web Product Metadata Extraction by your desktop Browser as web scraping tool (Amazon Nova Act - aka Computer Use)

A Python web scraping tool that uses Amazon Nova Act (as of 2025 August, Nova Act is in public preview for user with USA IP address to apply for API Key) to automatically extract comprehensive product information from the Goyard luxury goods website.

## 🎯 Features

- **Automated Web Navigation**: Handles cookies, search functionality, and product page navigation
- **Comprehensive Data Extraction**: Extracts 10 different product metadata fields
- **Color Variation Detection**: Automatically clicks through all available color options
- **Structured Output**: Provides both formatted display and JSON export
- **Error Handling**: Robust error handling with detailed logging
- **Security First**: No hardcoded API keys or sensitive information

## 📊 Extracted Data Fields

| Field | Description | Example |
|-------|-------------|---------|
| `product_name` | Product title | "Courrier Messenger Bag" |
| `product_description` | Main product description | "Sleek, lightweight and compact..." |
| `product_colours` | All available colors | "BLACK BLACK & TAN GREEN NAVY BLUE GREY" |
| `product_detail_description` | Complete specifications | "Material: Goyardine Canvas..." |
| `product_material` | Materials used | "Goyardine Canvas & Chevroches Calfskin" |
| `product_dimensions` | Size measurements | "Length: 32 cm, Width: 4 cm, Height: 25 cm" |
| `product_made_in` | Country of origin | "France" |
| `product_id` | Product identifier | "COURSIMMLTY51CL51P" |
| `care_Usage_precaution` | Usage warnings | "Do not graze or rub against rough surfaces..." |
| `care_advice` | Care instructions | "Clean with a soft cloth..." |

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Nova Act API key (from Amazon)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/danielpeggy/goyard-product-scraper.git
   cd goyard-product-scraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Also, please visit nova.amazon.com and review the instruction to install the SDK and generate the API key.

3. **Set up your API key**
   ```bash
   export NOVA_ACT_API_KEY='your-nova-act-api-key-here'
   ```

4. **Run the scraper**
   ```bash
   python goyard_scraper_secure.py
   ```

### Alternative API Key Setup

You can also create a `.env` file in the project root:
```
NOVA_ACT_API_KEY=your-nova-act-api-key-here
```

## 📖 Usage

### Basic Usage

```python
from goyard_scraper_secure import GoyardScraper

# Initialize scraper (reads API key from environment)
scraper = GoyardScraper()

# Extract product metadata
product_data = scraper.extract_product_metadata()

# Display results
scraper.display_results(product_data)

# Save to file
scraper.save_results(product_data, "my_extraction.json")
```

### Custom Product ID

```python
# Extract data for a specific product
product_data = scraper.extract_product_metadata(product_id="CUSTOM_PRODUCT_ID")
```

### Programmatic Usage

```python
# Initialize with API key directly (not recommended for production)
scraper = GoyardScraper(api_key="your-api-key")

# Extract and process data
product_data = scraper.extract_product_metadata()
if product_data:
    print(f"Product: {product_data['product_name']}")
    print(f"Colors: {product_data['product_colours']}")
```

## 🏗️ Project Structure

```
goyard-product-scraper/
├── goyard_scraper_secure.py    # Main scraper class
├── requirements.txt            # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Git ignore file
├── examples/                  # Usage examples
│   └── basic_usage.py
├── tests/                     # Unit tests
│   └── test_scraper.py
└── docs/                      # Additional documentation
    ├── API.md                 # API documentation
    └── TROUBLESHOOTING.md     # Common issues and solutions
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `NOVA_ACT_API_KEY` | Your Nova Act API key | Yes |

### Supported Product IDs

Currently tested with:
- `COURSIMMLTY01CL03P` (Courrier Messenger Bag)

## 📈 Success Metrics

The tool provides detailed success metrics:

```
📊 SUCCESS SUMMARY:
   • Fields extracted: 10/10
   • Success rate: 100.0%
   🎨 Colors found: 5
   🎨 Color list: BLACK, BLACK & TAN, GREEN, NAVY BLUE, GREY
   🏆 PERFECT EXTRACTION!
```

## 🛠️ Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

This project follows PEP 8 style guidelines. Format code with:

```bash
black goyard_scraper_secure.py
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔒 Security

- **Never commit API keys** to the repository
- **Use environment variables** for sensitive configuration
- **Review logs** before sharing to ensure no sensitive data is exposed
- **Rotate API keys** regularly

## ⚠️ Legal and Ethical Considerations

- **Respect robots.txt**: Always check the website's robots.txt file
- **Rate limiting**: The tool includes built-in delays to avoid overwhelming servers
- **Terms of service**: Ensure your usage complies with Goyard's terms of service
- **Personal use**: This tool is intended for educational and personal use only

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   ValueError: Nova Act API key is required
   ```
   **Solution**: Set the `NOVA_ACT_API_KEY` environment variable

2. **Network Timeout**
   ```
   ActExceededMaxStepsError: Allowed Steps Exceeded
   ```
   **Solution**: Check your internet connection and try again

3. **Product Not Found**
   ```
   Product extraction failed
   ```
   **Solution**: Verify the product ID exists on the Goyard website

### Debug Mode

Enable verbose logging:
```bash
export NOVA_ACT_DEBUG=1
python goyard_scraper_secure.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Amazon Nova Act** - For providing the web automation framework
- **Goyard** - For creating beautiful luxury products to analyze
- **Python Community** - For the excellent libraries and tools

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/danielpeggy/goyard-product-scraper/issues)
- **Discussions**: [GitHub Discussions](https://github.com/danielpeggy/goyard-product-scraper/discussions)
- **Email**: danielpeggy@gmail.com

## 🔄 Changelog

### v1.0.0 (2025-01-26)
- Initial release
- Complete product metadata extraction
- Support for all 5 color variations
- Comprehensive error handling
- Security-first design

---

**⭐ If this project helped you, please give it a star on GitHub!**
