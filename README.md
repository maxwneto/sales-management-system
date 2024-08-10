# Sales Management System

## Overview

This Sales Management System is a simple yet comprehensive application developed in Python using the MVC (Model-View-Controller) architecture. The system is designed to manage clients, employees, suppliers, categories, products, and sales through a command-line interface (CLI). It supports full CRUD operations across all entities, including the management of stock levels and sales reports.

## Features

- **Manage Clients**: Add, list, edit, delete, and manage clients.
- **Manage Employees**: Add, list, edit, delete, and manage employees.
- **Manage Suppliers**: Add, list, edit, delete, and manage suppliers.
- **Manage Categories**: Add, list, edit, delete, and manage product categories.
- **Manage Products**: Add, list, edit, delete, and manage products, including associating them with categories and managing stock levels.
- **Manage Sales**: Register sales, list sales reports, filter sales by date, and view top-selling products and top clients.
- **Cash Register Management**: Track total sales volume, supporting future functionalities like handling returns and managing cash flow.

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

1. **Manage Clients**: Allows you to add, list, edit, and delete clients.
2. **Manage Employees**: Allows you to add, list, edit, and delete employees.
3. **Manage Suppliers**: Allows you to add, list, edit, and delete suppliers.
4. **Manage Categories**: Allows you to add, list, edit, and delete product categories.
5. **Manage Products**: Allows you to add, list, edit, and delete products, associating them with a category and managing stock levels.
6. **Manage Sales**: Allows you to register sales, view sales reports, filter sales by date, view top-selling products, and identify top clients.
7. **Exit**: Closes the application.

### Example Workflow

1. **Add a Category**: Before adding a product, ensure you have categories set up. You can add a category through the "Manage Categories" option.
2. **Add a Product**: Add a product by selecting a category from the available list, then provide the product name, price, and initial stock quantity.
3. **Register a Sale**: Once products are added, you can register a sale by selecting a client and the products purchased, with automatic stock management.
4. **View Sales Reports**: After registering sales, you can view comprehensive sales reports, filter by date, and analyze top-performing products and clients.

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
├── db_file/                  # Directory for storing JSON data files
│   ├── clients.json
│   ├── employees.json
│   ├── suppliers.json
│   ├── products.json
│   ├── sales.json
│   ├── categories.json
│   └── cash_register.json
│
└── main.py
```

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. Please ensure that your code follows the PEP 8 style guide and is well-documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Key Updates:

1. **Expanded Features**: Added details about the full CRUD operations available for all entities, as well as the Cash Register management.
2. **Example Workflow**: Provided a clearer workflow example that incorporates all key functionalities, including stock management during sales.
3. **Project Structure**: Updated the structure to reflect the dedicated `db_file/` directory for JSON data files.