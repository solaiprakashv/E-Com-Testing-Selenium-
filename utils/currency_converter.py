"""
Currency Converter Utility
Converts USD to INR for test reporting
"""


class CurrencyConverter:
    # Exchange rate (approximate - you can update this)
    USD_TO_INR = 83.0  # 1 USD = 83 INR (approximate)
    
    @staticmethod
    def usd_to_inr(usd_amount):
        """
        Convert USD to INR
        
        Args:
            usd_amount (float): Amount in USD
            
        Returns:
            float: Amount in INR
        """
        return round(usd_amount * CurrencyConverter.USD_TO_INR, 2)
    
    @staticmethod
    def format_inr(amount):
        """
        Format amount in Indian Rupee format
        
        Args:
            amount (float): Amount to format
            
        Returns:
            str: Formatted string with ₹ symbol
        """
        return f"₹{amount:,.2f}"
    
    @staticmethod
    def format_usd(amount):
        """
        Format amount in USD format
        
        Args:
            amount (float): Amount to format
            
        Returns:
            str: Formatted string with $ symbol
        """
        return f"${amount:,.2f}"
    
    @staticmethod
    def parse_usd(price_string):
        """
        Parse USD price string to float
        
        Args:
            price_string (str): Price string like "$29.99"
            
        Returns:
            float: Parsed amount
        """
        return float(price_string.replace("$", "").replace(",", "").strip())
    
    @staticmethod
    def convert_and_format(usd_string):
        """
        Convert USD string to INR formatted string
        
        Args:
            usd_string (str): USD price like "$29.99"
            
        Returns:
            str: INR formatted price like "₹2,489.17"
        """
        usd_amount = CurrencyConverter.parse_usd(usd_string)
        inr_amount = CurrencyConverter.usd_to_inr(usd_amount)
        return CurrencyConverter.format_inr(inr_amount)
    
    @staticmethod
    def get_dual_currency_display(usd_string):
        """
        Get both USD and INR display
        
        Args:
            usd_string (str): USD price like "$29.99"
            
        Returns:
            str: Dual currency display like "$29.99 (₹2,489.17)"
        """
        inr_display = CurrencyConverter.convert_and_format(usd_string)
        return f"{usd_string} ({inr_display})"
