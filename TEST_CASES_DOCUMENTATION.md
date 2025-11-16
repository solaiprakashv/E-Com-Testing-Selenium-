# Test Cases Documentation

## E-Commerce Automation Test Suite

### Test Environment
- **Application URL**: https://www.saucedemo.com/
- **Browser**: Chrome (latest)
- **Framework**: Selenium + PyTest
- **Language**: Python 3.8+

---

## Test Suite 1: Login Functionality

| Test ID | Test Case | Priority | Steps | Expected Result | Status |
|---------|-----------|----------|-------|-----------------|--------|
| TC_001 | Verify login with valid credentials | High | 1. Navigate to login page<br>2. Enter username: "standard_user"<br>3. Enter password: "secret_sauce"<br>4. Click Login | User redirected to Products page | ✅ Pass |
| TC_002 | Verify login with invalid username | High | 1. Navigate to login page<br>2. Enter invalid username<br>3. Enter valid password<br>4. Click Login | Error message: "Username and password do not match" | ✅ Pass |
| TC_003 | Verify login with invalid password | High | 1. Navigate to login page<br>2. Enter valid username<br>3. Enter invalid password<br>4. Click Login | Error message: "Username and password do not match" | ✅ Pass |
| TC_004 | Verify login with empty credentials | Medium | 1. Navigate to login page<br>2. Leave fields empty<br>3. Click Login | Error message: "Username is required" | ✅ Pass |
| TC_005 | Verify login with locked user | Medium | 1. Navigate to login page<br>2. Enter "locked_out_user"<br>3. Enter valid password<br>4. Click Login | Error message: "Sorry, this user has been locked out" | ✅ Pass |

---

## Test Suite 2: Products Page Functionality

| Test ID | Test Case | Priority | Steps | Expected Result | Status |
|---------|-----------|----------|-------|-----------------|--------|
| TC_006 | Verify products page loads correctly | High | 1. Login with valid credentials<br>2. Verify page loads | Products page displayed with title "Products" | ✅ Pass |
| TC_007 | Verify products are displayed | High | 1. Login successfully<br>2. Count products on page | 6 products should be visible | ✅ Pass |
| TC_008 | Verify product names are visible | Medium | 1. Login successfully<br>2. Check product names | All product names should be displayed | ✅ Pass |
| TC_009 | Verify product prices are visible | Medium | 1. Login successfully<br>2. Check product prices | All prices displayed with $ symbol | ✅ Pass |

---

## Test Suite 3: Add to Cart Functionality

| Test ID | Test Case | Priority | Steps | Expected Result | Status |
|---------|-----------|----------|-------|-----------------|--------|
| TC_010 | Verify add single product to cart | High | 1. Login successfully<br>2. Click "Add to Cart" for one product<br>3. Check cart badge | Cart badge shows "1" | ✅ Pass |
| TC_011 | Verify add multiple products to cart | High | 1. Login successfully<br>2. Add 3 products to cart<br>3. Check cart badge | Cart badge shows "3" | ✅ Pass |
| TC_012 | Verify cart quantity | High | 1. Login and add product<br>2. Navigate to cart<br>3. Check quantity | Quantity should be "1" | ✅ Pass |
| TC_013 | Validate cart total price | High | 1. Login and add 2 products<br>2. Navigate to cart<br>3. Calculate total | Total equals sum of product prices | ✅ Pass |
| TC_014 | Verify product details in cart | Medium | 1. Login and add product<br>2. Navigate to cart<br>3. Check details | Product name, price with $ displayed | ✅ Pass |
| TC_015 | Verify remove item from cart | High | 1. Add 2 products to cart<br>2. Navigate to cart<br>3. Remove one item | Cart count reduces to 1 | ✅ Pass |
| TC_016 | Verify empty cart | Medium | 1. Login successfully<br>2. Navigate to cart without adding items | Cart should be empty, count = 0 | ✅ Pass |

---

## Test Suite 4: Logout Functionality

| Test ID | Test Case | Priority | Steps | Expected Result | Status |
|---------|-----------|----------|-------|-----------------|--------|
| TC_017 | Verify logout successfully | High | 1. Login successfully<br>2. Click menu button<br>3. Click Logout | User redirected to login page | ✅ Pass |
| TC_018 | Verify logout and re-login | Medium | 1. Login and logout<br>2. Login again with valid credentials | User can login again successfully | ✅ Pass |

---

## Test Execution Summary

| Metric | Value |
|--------|-------|
| Total Test Cases | 18 |
| Passed | 18 |
| Failed | 0 |
| Blocked | 0 |
| Pass Rate | 100% |
| Execution Time | ~45 seconds |

---

## Test Data

### Valid Credentials
- **Username**: standard_user
- **Password**: secret_sauce

### Invalid Test Data
- **Invalid Username**: invalid_user
- **Invalid Password**: wrong_password
- **Locked User**: locked_out_user

---

## Defects Found
No defects found during test execution. All test cases passed successfully.

---

## Test Coverage

### Functional Areas Covered
✅ User Authentication (Login/Logout)  
✅ Product Listing and Display  
✅ Shopping Cart Operations  
✅ Price Calculations  
✅ Error Handling and Validation  

### Functional Areas Not Covered
❌ Checkout Process  
❌ Payment Processing  
❌ User Registration  
❌ Order History  
❌ Product Search/Filter  

---

## Recommendations
1. Extend test coverage to checkout flow
2. Add performance testing for page load times
3. Implement cross-browser testing
4. Add API testing for backend validation
5. Integrate with CI/CD pipeline

---

**Document Version**: 1.0  
**Last Updated**: 2024  
**Prepared By**: QA Automation Engineer
