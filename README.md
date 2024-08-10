# Sales Management System

## Overview

This is a simple Sales Management System developed in Python using the MVC (Model-View-Controller) architecture. The system allows you to manage clients, employees, suppliers, categories, products, and sales through a command-line interface (CLI).

## Features

- **Manage Clients**: Add, list, and manage clients.
- **Manage Employees**: Add, list, and manage employees.
- **Manage Suppliers**: Add, list, and manage suppliers.
- **Manage Categories**: Add, list, and manage product categories.
- **Manage Products**: Add, list, and manage products, including associating them with categories.
- **Manage Sales**: Register sales, list sales reports, filter sales by date, and view top-selling products and top clients.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/maxwneto/sales-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sales-management-system
   ```

3. Ensure you have Python installed. This project is compatible with Python 3.6 and above.

## Usage

To start the application, run the `main.py` file:

```bash
python main.py
```

You will be presented with a main menu where you can choose to manage clients, employees, suppliers, categories, products, or sales. The interface is command-line based, and you will interact with the system by entering the numbers corresponding to the actions you wish to perform.

### Main Menu

1. **Manage Clients**: Allows you to add new clients and view the list of existing clients.
2. **Manage Employees**: Allows you to add new employees and view the list of existing employees.
3. **Manage Suppliers**: Allows you to add new suppliers and view the list of existing suppliers.
4. **Manage Categories**: Allows you to add new product categories and view the list of existing categories.
5. **Manage Products**: Allows you to add new products, associating them with a category, and view the list of existing products.
6. **Manage Sales**: Allows you to register sales, view sales reports, filter sales by date, and view top-selling products and clients.
7. **Exit**: Closes the application.

### Example Workflow

1. **Add a Category**: Before adding a product, ensure you have categories set up. You can add a category through the "Manage Categories" option.
2. **Add a Product**: Add a product by selecting a category from the available list, then provide the product name and price.
3. **Register a Sale**: Once products are added, you can register a sale by selecting a client and the products purchased.

## Project Structure

```plaintext
sales_management_system/
│
├── models/
│   ├── person.py
│   ├── client.py
│   ├── employee.py
│   ├── supplier.py
│   ├── category.py
│   ├── product.py
│   ├── sale.py
│   └── __init__.py
│
├── dal/
│   ├── data_manager.py
│   └── __init__.py
│
├── controllers/
│   ├── client_controller.py
│   ├── employee_controller.py
│   ├── supplier_controller.py
│   ├── product_controller.py
│   ├── sale_controller.py
│   ├── category_controller.py
│   └── __init__.py
│
├── views/
│   ├── client_view.py
│   ├── employee_view.py
│   ├── supplier_view.py
│   ├── product_view.py
│   ├── sale_view.py
│   ├── category_view.py
│   └── __init__.py
│
└── main.py
```

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. Please ensure that your code follows the PEP 8 style guide and is well-documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
