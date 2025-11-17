# Implementation Plan

- [x] 1. Setup testing infrastructure
  - Create tests directory structure with __init__.py files
  - Create pytest.ini configuration file
  - Create .coveragerc configuration file
  - Update pyproject.toml with test dependencies (pytest, pytest-cov, pytest-asyncio)
  - _Requirements: 5.1, 5.2_

- [x] 2. Create responsive utilities module
  - [x] 2.1 Create utils directory and responsive.py file
    - Implement Breakpoint enum with MOBILE, TABLET, DESKTOP values
    - Implement ResponsiveConfig class with static methods
    - Implement get_breakpoint() method to detect breakpoint from width
    - Implement get_font_size() method with scaling logic
    - Implement get_spacing() method with scaling logic
    - Implement get_grid_columns() method returning columns per breakpoint
    - Implement get_container_padding() method returning padding dict
    - _Requirements: 1.1, 1.2, 1.3, 1.4_

- [x] 3. Enhance theme module with responsive functions
  - [x] 3.1 Add responsive helper functions to theme.py
    - Implement get_responsive_font_size() function
    - Implement get_responsive_padding() function
    - Implement get_responsive_spacing() function
    - Update existing functions to support responsive parameters
    - _Requirements: 1.4, 3.3, 4.3_

- [x] 4. Create test fixtures and base test infrastructure
  - [x] 4.1 Create conftest.py with reusable fixtures
    - Implement mock_page fixture with basic Page mock
    - Implement mobile_page fixture (width=400px)
    - Implement tablet_page fixture (width=768px)
    - Implement desktop_page fixture (width=1920px)
    - Implement theme_colors fixture with COLORS dict
    - _Requirements: 5.5_

- [x] 5. Implement tests for theme module
  - [x] 5.1 Create test_theme.py with comprehensive theme tests
    - Write test for get_theme() returns valid Theme object
    - Write test for get_button_style() returns ButtonStyle with correct properties
    - Write test for get_text_style() with default parameters
    - Write test for get_text_style() with custom size, color, weight
    - Write test for get_shadow() returns BoxShadow with correct properties
    - Write test for get_responsive_font_size() with mobile width
    - Write test for get_responsive_font_size() with tablet width
    - Write test for get_responsive_font_size() with desktop width
    - Write test for get_responsive_padding() with different widths
    - Write test for get_responsive_spacing() with different widths
    - _Requirements: 2.2_

- [x] 6. Implement tests for responsive module
  - [x] 6.1 Create test_responsive.py with responsive system tests
    - Write test for get_breakpoint() with mobile width (400px)
    - Write test for get_breakpoint() with tablet width (768px)
    - Write test for get_breakpoint() with desktop width (1920px)
    - Write test for get_breakpoint() with edge cases (600px, 900px)
    - Write test for get_font_size() for each breakpoint
    - Write test for get_spacing() for each breakpoint
    - Write test for get_grid_columns() returns correct columns per breakpoint
    - Write test for get_container_padding() returns correct padding per breakpoint
    - _Requirements: 2.5_

- [x] 7. Refactor home page for full responsiveness
  - [x] 7.1 Update pages/home.py with responsive system
    - Import ResponsiveConfig and use get_breakpoint()
    - Update title font size using get_responsive_font_size()
    - Update subtitle font size using get_responsive_font_size()
    - Update button padding using get_responsive_padding()
    - Update spacing between elements using get_responsive_spacing()
    - Ensure buttons wrap properly on mobile
    - Test layout at 375px, 768px, 1920px widths
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

- [x] 8. Refactor services page for full responsiveness
  - [x] 8.1 Update pages/services.py with responsive grid system
    - Import ResponsiveConfig and detect breakpoint
    - Update GridView runs_count based on breakpoint (mobile: 1, tablet: 2, desktop: 3)
    - Update card padding using get_responsive_padding()
    - Update icon sizes using get_responsive_font_size()
    - Update title and description font sizes responsively
    - Ensure cards have consistent spacing across breakpoints
    - Remove hardcoded width calculations
    - _Requirements: 1.1, 1.2, 1.3, 3.1, 4.1_

- [x] 9. Refactor portfolio page for full responsiveness
  - [x] 9.1 Update pages/portfolio.py with responsive images and layout
    - Import ResponsiveConfig and detect breakpoint
    - Update image dimensions using responsive calculations
    - Update ResponsiveRow col configuration for proper grid
    - Update project card padding using get_responsive_padding()
    - Update font sizes for title and description
    - Update technology tag sizes and spacing
    - Ensure images use fit=COVER and proper border_radius
    - _Requirements: 1.1, 1.2, 1.3, 3.2, 4.2, 6.1, 6.3, 6.4_

- [x] 10. Refactor coins page for full responsiveness
  - [x] 10.1 Update pages/coins.py with responsive chart and layout
    - Import ResponsiveConfig and detect breakpoint
    - Update chart container height based on breakpoint (mobile: 300px, tablet: 350px, desktop: 400px)
    - Update title and subtitle font sizes responsively
    - Update container padding using get_responsive_padding()
    - Ensure loading indicator is properly centered
    - Ensure error messages are readable on all breakpoints
    - Optimize async loading for better performance
    - _Requirements: 1.1, 1.2, 1.3, 6.2, 6.5_

- [x] 11. Refactor contact page for full responsiveness
  - [x] 11.1 Update pages/contact.py with responsive form layout
    - Import ResponsiveConfig and detect breakpoint
    - Update form field widths (mobile: 100%, desktop: 400px)
    - Update title font size responsively
    - Update container padding using get_responsive_padding()
    - Update spacing between form fields
    - Ensure validation messages are visible on all breakpoints
    - Ensure submit button is properly sized and positioned
    - _Requirements: 1.1, 1.2, 1.3, 4.4, 7.1, 7.2, 7.3, 7.4, 7.5_

- [x] 12. Refactor about page for full responsiveness
  - [x] 12.1 Update pages/about.py with responsive content layout
    - Import ResponsiveConfig and detect breakpoint
    - Update title font sizes responsively
    - Update container max-width based on breakpoint
    - Update padding using get_responsive_padding()
    - Update spacing between sections using get_responsive_spacing()
    - Ensure text is readable on all breakpoints
    - _Requirements: 1.1, 1.2, 1.3_

- [x] 13. Refactor app.py header and footer for full responsiveness
  - [x] 13.1 Update app.py with responsive header
    - Update create_header() to use ResponsiveConfig
    - Update logo font size responsively
    - Update navigation button sizes and spacing
    - Ensure mobile menu (PopupMenuButton) works correctly
    - Update toolbar_height calculation using responsive values
    - _Requirements: 1.1, 1.2, 1.3, 3.3_

  - [x] 13.2 Update app.py with responsive footer
    - Update create_footer() to use ResponsiveConfig
    - Update footer text sizes responsively
    - Update icon sizes responsively
    - Update padding and spacing using responsive functions
    - Ensure footer is always visible and properly positioned
    - _Requirements: 1.1, 1.2, 1.3, 3.4_

- [x] 14. Implement tests for home page
  - [x] 14.1 Create tests/pages/test_home.py
    - Write test for home_content() returns valid Container
    - Write test for home_content() with mobile_page fixture
    - Write test for home_content() with tablet_page fixture
    - Write test for home_content() with desktop_page fixture
    - Write test for button navigation handlers
    - _Requirements: 2.1_

- [x] 15. Implement tests for services page
  - [x] 15.1 Create tests/pages/test_services.py
    - Write test for services_content() returns valid Container
    - Write test for create_card() function with different parameters
    - Write test for GridView runs_count on mobile (should be 1)
    - Write test for GridView runs_count on tablet (should be 2)
    - Write test for GridView runs_count on desktop (should be 3)
    - Write test for services list has 8 items
    - Write test for technologies list has 8 items
    - _Requirements: 2.1_

- [x] 16. Implement tests for portfolio page
  - [x] 16.1 Create tests/pages/test_portfolio.py
    - Write test for portfolio_content() returns valid Container
    - Write test for create_project_card() function
    - Write test for projects list has 3 items
    - Write test for image dimensions on mobile
    - Write test for image dimensions on desktop
    - Write test for ResponsiveRow configuration
    - _Requirements: 2.1_

- [x] 17. Implement tests for coins page
  - [x] 17.1 Create tests/pages/test_coins.py
    - Write test for currency_chart_content() returns valid Container
    - Write test for create_chart() with valid data
    - Write test for create_chart() with empty data
    - Write test for fetch_usd_brl_data() with mocked httpx
    - Write test for cache mechanism (should not refetch within 5 minutes)
    - Write test for loading state display
    - Write test for error state display
    - _Requirements: 2.1, 2.5_

- [x] 18. Implement tests for contact page
  - [x] 18.1 Create tests/pages/test_contact.py
    - Write test for contact_content() returns valid Container
    - Write test for handle_submit() with empty fields (should show error)
    - Write test for handle_submit() with valid data (should show success)
    - Write test for form field clearing after successful submit
    - Write test for field widths on mobile vs desktop
    - _Requirements: 2.1, 2.4, 7.1, 7.2, 7.3, 7.4_

- [x] 19. Implement tests for about page
  - [x] 19.1 Create tests/pages/test_about.py
    - Write test for about_content() returns valid Container
    - Write test for about_content() with mobile_page fixture
    - Write test for about_content() with desktop_page fixture
    - Write test for container max-width on different breakpoints
    - _Requirements: 2.1_

- [x] 20. Implement tests for app.py main functionality
  - [x] 20.1 Create tests/test_app.py
    - Write test for create_header() with is_mobile=True
    - Write test for create_header() with is_mobile=False
    - Write test for create_footer() returns valid Container
    - Write test for route_change() with each route (/, /services, /about, /contact, /coins, /portfolio)
    - Write test for handle_login_click() opens dialog
    - Write test for login_with_google() shows success SnackBar
    - Write test for login_with_apple() shows success SnackBar
    - Write test for login_with_x() shows success SnackBar
    - Write test for close_dialog() closes dialog
    - _Requirements: 2.1, 2.3, 8.1, 8.2, 8.3, 8.4_

- [x] 21. Run full test suite and generate coverage report
  - Execute pytest with coverage flags
  - Review coverage report and identify gaps
  - Ensure coverage >= 80%
  - Ensure all tests pass (0 failures)
  - Ensure execution time < 30 seconds
  - Generate HTML coverage report
  - _Requirements: 5.3, 5.4_

- [x] 22. Update documentation
  - Update README.md with testing instructions
  - Add section about running tests
  - Add section about responsive design breakpoints
  - Add section about test coverage
  - Document responsive utilities usage
  - _Requirements: 5.1_
