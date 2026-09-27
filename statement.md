# Project Statement

## Problem statement

College students often struggle to track their daily expenses and manage their monthly budgets effectively without complex financial software. Many rely on mental calculations or unstructured notes, leading to overspending and financial stress. There is a need for a lightweight, easily accessible, and visually clear tool to log expenses and monitor spending habits directly from a personal computer.

## Scope of the project

This project delivers a terminal-based Python application that allows users to set a baseline monthly budget, log daily expenses by specific categories, and view real-time remaining balances. The application operates entirely locally, utilizing a JSON file for data persistence. It is scoped strictly to manual entry and local analytics, meaning it does not integrate with real bank accounts, external APIs, or cloud databases.

## Target users

* College and university students managing limited monthly allowances.


* Young adults looking for a simple, distraction-free personal budgeting tool.


* Individuals who prefer localized, console-based software over web applications.



## High-level features

* **User Management:** Multi-user profile creation that isolates data per user.


* **Expense Logging:** Create, read, and append specific expense records including amount, category, and description.


* **Live Budget Tracking:** Real-time calculation and display of the remaining monthly budget after every logged transaction.


* **Visual Analytics:** Automated ASCII bar chart generation to visualize spending proportions across different categories without needing a graphical user interface.


* **Data Persistence:** Automatic local saving and loading of all data using standard JSON formatting. 
