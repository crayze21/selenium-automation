# =============================================================================
# locators/locators.py
# All Selenium locators for Toreja Medical Clinic PMS
# URL: http://torejamedicalclinic.wuaze.com
# =============================================================================
# Usage: driver.find_element(*LoginPage.USERNAME_INPUT)
# =============================================================================

from selenium.webdriver.common.by import By


# =============================================================================
# PAGE URLS
# =============================================================================
class URLs:
    BASE             = "http://torejamedicalclinic.wuaze.com"
    LOGIN            = "http://torejamedicalclinic.wuaze.com/index.php"
    DASHBOARD        = "http://torejamedicalclinic.wuaze.com/dashboard.php"
    NEW_PRESCRIPTION = "http://torejamedicalclinic.wuaze.com/new_prescription.php"
    PATIENTS         = "http://torejamedicalclinic.wuaze.com/patients.php"
    PATIENT_HISTORY  = "http://torejamedicalclinic.wuaze.com/patient_history.php"
    MEDICINES        = "http://torejamedicalclinic.wuaze.com/medicines.php"
    MEDICINE_DETAILS = "http://torejamedicalclinic.wuaze.com/medicine_details.php"
    REPORTS          = "http://torejamedicalclinic.wuaze.com/reports.php"
    USERS            = "http://torejamedicalclinic.wuaze.com/users.php"
    LOGOUT           = "http://torejamedicalclinic.wuaze.com/logout.php"


# =============================================================================
# LOGIN PAGE  (index.php)
# =============================================================================
class LoginPage:
    LOGO              = (By.ID,           "system-logo")
    USERNAME_INPUT    = (By.ID,           "user_name")
    USERNAME_NAME     = (By.NAME,         "user_name")
    PASSWORD_INPUT    = (By.ID,           "password")
    PASSWORD_NAME     = (By.NAME,         "password")
    LOGIN_BUTTON      = (By.NAME,         "login")
    LOGIN_BUTTON_CSS  = (By.CSS_SELECTOR, "button[name='login']")
    ERROR_MESSAGE     = (By.CSS_SELECTOR, "p.text-danger, p[style*='color']")
    SUBTITLE          = (By.XPATH,        "//p[contains(text(),'Please enter your login credentials')]")


# =============================================================================
# SHARED: NAVIGATION / SIDEBAR  (all authenticated pages)
# =============================================================================
class NavBar:
    # Top bar
    TOGGLE_SIDEBAR       = (By.CSS_SELECTOR, "a[data-widget='pushmenu']")
    BRAND_LINK           = (By.CSS_SELECTOR, "a.navbar-brand")
    WELCOME_TEXT         = (By.CSS_SELECTOR, "div.login-user")

    # Sidebar panel
    SIDEBAR              = (By.CSS_SELECTOR, "aside.main-sidebar")
    USER_AVATAR          = (By.CSS_SELECTOR, "div.user-panel img.img-circle")
    USER_PANEL_NAME      = (By.CSS_SELECTOR, "div.user-panel div.info a")

    # Main menu items (li wrappers — for state checks)
    MENU_DASHBOARD       = (By.ID,           "mnu_dashboard")
    MENU_PATIENTS        = (By.ID,           "mnu_patients")
    MENU_MEDICINES       = (By.ID,           "mnu_medicines")
    MENU_REPORTS         = (By.ID,           "mnu_reports")
    MENU_USERS           = (By.ID,           "mnu_users")

    # Main menu links (clickable anchors)
    MENU_DASHBOARD_LINK  = (By.CSS_SELECTOR, "#mnu_dashboard > a")
    MENU_PATIENTS_LINK   = (By.CSS_SELECTOR, "#mnu_patients > a")
    MENU_MEDICINES_LINK  = (By.CSS_SELECTOR, "#mnu_medicines > a")
    MENU_REPORTS_LINK    = (By.CSS_SELECTOR, "#mnu_reports > a")
    MENU_USERS_LINK      = (By.CSS_SELECTOR, "#mnu_users > a")

    # Sub-menu items
    SUBMENU_NEW_RX       = (By.ID,           "mi_new_prescription")
    SUBMENU_PATIENTS     = (By.ID,           "mi_patients")
    SUBMENU_HISTORY      = (By.ID,           "mi_patient_history")
    SUBMENU_ADD_MED      = (By.ID,           "mi_medicines")
    SUBMENU_MED_DETAILS  = (By.ID,           "mi_medicine_details")
    SUBMENU_REPORTS      = (By.ID,           "mi_reports")

    # Logout
    LOGOUT_LINK          = (By.CSS_SELECTOR, "a[href='logout.php']")

    # Footer
    FOOTER               = (By.CSS_SELECTOR, "footer.main-footer")


# =============================================================================
# DASHBOARD PAGE  (dashboard.php)
# =============================================================================
class DashboardPage:
    PAGE_HEADING       = (By.CSS_SELECTOR, "section.content-header h1")

    # Stat boxes (containers)
    BOX_TODAY          = (By.CSS_SELECTOR, "div.small-box.bg-info")
    BOX_WEEK           = (By.CSS_SELECTOR, "div.small-box.bg-purple")
    BOX_MONTH          = (By.CSS_SELECTOR, "div.small-box.bg-fuchsia")
    BOX_YEAR           = (By.CSS_SELECTOR, "div.small-box.bg-maroon")

    # Stat counts
    COUNT_TODAY        = (By.CSS_SELECTOR, "div.small-box.bg-info h3")
    COUNT_WEEK         = (By.CSS_SELECTOR, "div.small-box.bg-purple h3")
    COUNT_MONTH        = (By.CSS_SELECTOR, "div.small-box.bg-fuchsia h3")
    COUNT_YEAR         = (By.CSS_SELECTOR, "div.small-box.bg-maroon h3")


# =============================================================================
# PATIENTS PAGE  (patients.php)
# =============================================================================
class PatientsPage:
    PAGE_HEADING        = (By.CSS_SELECTOR,  "section.content-header h1")
    FORM_HEADING        = (By.XPATH,         "//h3[text()='Add Patients']")

    # Form fields
    PATIENT_NAME        = (By.ID,            "patient_name")
    ADDRESS             = (By.ID,            "address")
    CNIC                = (By.ID,            "cnic")
    DATE_OF_BIRTH_WRAP  = (By.ID,            "date_of_birth")
    DATE_OF_BIRTH_INPUT = (By.NAME,          "date_of_birth")
    PHONE_NUMBER        = (By.ID,            "phone_number")
    GENDER              = (By.ID,            "gender")
    SAVE_BTN            = (By.ID,            "save_Patient")

    # DataTable
    TABLE               = (By.ID,            "all_patients")
    TABLE_WRAPPER       = (By.ID,            "all_patients_wrapper")
    SEARCH_INPUT        = (By.CSS_SELECTOR,  "#all_patients_filter input")
    PAGE_INFO           = (By.ID,            "all_patients_info")
    PAGINATE            = (By.ID,            "all_patients_paginate")
    PREV_BTN            = (By.ID,            "all_patients_previous")
    NEXT_BTN            = (By.ID,            "all_patients_next")

    # Table headers
    TH_SNO              = (By.XPATH,         "//table[@id='all_patients']//th[1]")
    TH_NAME             = (By.XPATH,         "//table[@id='all_patients']//th[2]")
    TH_ADDRESS          = (By.XPATH,         "//table[@id='all_patients']//th[3]")
    TH_CNIC             = (By.XPATH,         "//table[@id='all_patients']//th[4]")
    TH_DOB              = (By.XPATH,         "//table[@id='all_patients']//th[5]")
    TH_PHONE            = (By.XPATH,         "//table[@id='all_patients']//th[6]")
    TH_GENDER           = (By.XPATH,         "//table[@id='all_patients']//th[7]")
    TH_ACTION           = (By.XPATH,         "//table[@id='all_patients']//th[8]")

    # Export buttons
    BTN_COPY            = (By.XPATH,         "//button[.//span[text()='Copy']]")
    BTN_CSV             = (By.XPATH,         "//button[.//span[text()='CSV']]")
    BTN_EXCEL           = (By.XPATH,         "//button[.//span[text()='Excel']]")
    BTN_PDF             = (By.XPATH,         "//button[.//span[text()='PDF']]")
    BTN_PRINT           = (By.XPATH,         "//button[.//span[text()='Print']]")
    BTN_COL_VIS         = (By.XPATH,         "//button[.//span[text()='Column visibility']]")

    # Row action buttons (dynamic — use format with row index)
    # Example: (By.XPATH, f"//table[@id='all_patients']//tbody/tr[{row}]//a")
    EDIT_BTN_ROW        = "//table[@id='all_patients']//tbody/tr[{row}]//a[contains(@href,'edit')]"
    ANY_EDIT_BTN        = (By.CSS_SELECTOR,  "#all_patients tbody tr:first-child td:last-child a")


# =============================================================================
# NEW PRESCRIPTION PAGE  (new_prescription.php)
# =============================================================================
class NewPrescriptionPage:
    PAGE_HEADING        = (By.CSS_SELECTOR,  "section.content-header h1")

    # Patient select (Select2)
    PATIENT_SELECT      = (By.ID,            "patient")
    PATIENT_NAME_ARR    = (By.NAME,          "patient[]")
    PATIENT_SEARCH      = (By.CSS_SELECTOR,  "input[placeholder='Type Patient Name...']")
    PATIENT_S2_TRIGGER  = (By.CSS_SELECTOR,  "#patient + .select2-container .select2-selection")

    # Visit fields
    VISIT_DATE          = (By.NAME,          "visit_date")
    NEXT_VISIT_DATE     = (By.NAME,          "next_visit_date")
    BP_INPUT            = (By.NAME,          "bp")
    WEIGHT_INPUT        = (By.NAME,          "weight")
    DISEASE_INPUT       = (By.NAME,          "disease")

    # Medicine table
    ADD_ROW_BTN         = (By.ID,            "add_row")
    MEDICATION_TBODY    = (By.ID,            "medication_list")

    # Medicine row fields (first row) — use CSS nth-child for multiple rows
    MEDICINE_SELECT     = (By.NAME,          "medicine[]")
    MEDICINE_SEARCH     = (By.CSS_SELECTOR,  "input[placeholder='Type Medicine...']")
    FREQUENCY_SELECT    = (By.NAME,          "frequency[]")
    TIMING_SELECT       = (By.NAME,          "timing[]")
    QTY_INPUT           = (By.NAME,          "qty[]")
    DOSAGE_INPUT        = (By.NAME,          "dosage[]")

    # Table headers
    TH_MEDICINE         = (By.XPATH,         "//thead//th[1]")
    TH_PACKING          = (By.XPATH,         "//thead//th[2]")
    TH_FREQUENCY        = (By.XPATH,         "//thead//th[3]")
    TH_TIMING           = (By.XPATH,         "//thead//th[4]")
    TH_QTY              = (By.XPATH,         "//thead//th[5]")
    TH_DOSAGE           = (By.XPATH,         "//thead//th[6]")

    # Submit
    SAVE_BTN            = (By.NAME,          "submit")
    SAVE_BTN_CSS        = (By.CSS_SELECTOR,  "button[name='submit']")


# =============================================================================
# PATIENT HISTORY PAGE  (patient_history.php)
# =============================================================================
class PatientHistoryPage:
    PAGE_HEADING        = (By.CSS_SELECTOR,  "section.content-header h1")
    SECTION_HEADING     = (By.XPATH,         "//h3[text()='Search Patient History']")

    # Search
    PATIENT_SELECT      = (By.ID,            "patient")
    PATIENT_SEARCH      = (By.CSS_SELECTOR,  "input[placeholder='Type Patient Name...']")
    PATIENT_S2_TRIGGER  = (By.CSS_SELECTOR,  "#patient + .select2-container .select2-selection")
    SEARCH_BTN          = (By.ID,            "search")

    # Results table
    TABLE               = (By.ID,            "patient_history")
    HISTORY_TBODY       = (By.ID,            "history_data")

    TH_SNO              = (By.XPATH,         "//table[@id='patient_history']//th[1]")
    TH_VISIT_DATE       = (By.XPATH,         "//table[@id='patient_history']//th[2]")
    TH_DISEASE          = (By.XPATH,         "//table[@id='patient_history']//th[3]")
    TH_MEDICINE         = (By.XPATH,         "//table[@id='patient_history']//th[4]")
    TH_PACKING          = (By.XPATH,         "//table[@id='patient_history']//th[5]")
    TH_QTY              = (By.XPATH,         "//table[@id='patient_history']//th[6]")
    TH_DOSAGE           = (By.XPATH,         "//table[@id='patient_history']//th[7]")
    TH_INSTRUCTION      = (By.XPATH,         "//table[@id='patient_history']//th[8]")
    TH_ACTION           = (By.XPATH,         "//table[@id='patient_history']//th[9]")


# =============================================================================
# MEDICINES PAGE  (medicines.php)
# =============================================================================
class MedicinesPage:
    PAGE_HEADING        = (By.CSS_SELECTOR,  "section.content-header h1")
    FORM_HEADING        = (By.XPATH,         "//h3[text()='Add Medicine']")

    # Form
    MEDICINE_NAME       = (By.ID,            "medicine_name")
    MEDICINE_NAME_NAME  = (By.NAME,          "medicine_name")
    SAVE_BTN            = (By.ID,            "save_medicine")

    # DataTable
    TABLE               = (By.ID,            "all_medicines")
    TABLE_WRAPPER       = (By.ID,            "all_medicines_wrapper")
    SEARCH_INPUT        = (By.CSS_SELECTOR,  "#all_medicines_filter input")
    PAGE_INFO           = (By.ID,            "all_medicines_info")
    PAGINATE            = (By.ID,            "all_medicines_paginate")
    PREV_BTN            = (By.ID,            "all_medicines_previous")
    NEXT_BTN            = (By.ID,            "all_medicines_next")

    # Export buttons
    BTN_COPY            = (By.XPATH,         "//button[.//span[text()='Copy']]")
    BTN_CSV             = (By.XPATH,         "//button[.//span[text()='CSV']]")
    BTN_EXCEL           = (By.XPATH,         "//button[.//span[text()='Excel']]")
    BTN_PDF             = (By.XPATH,         "//button[.//span[text()='PDF']]")
    BTN_PRINT           = (By.XPATH,         "//button[.//span[text()='Print']]")

    ANY_EDIT_BTN        = (By.CSS_SELECTOR,  "#all_medicines tbody tr:first-child td:last-child a")


# =============================================================================
# MEDICINE DETAILS PAGE  (medicine_details.php)
# =============================================================================
class MedicineDetailsPage:
    PAGE_HEADING        = (By.CSS_SELECTOR,  "section.content-header h1")
    FORM_HEADING        = (By.XPATH,         "//h3[text()='Add Medicine Details']")

    # Form
    MEDICINE_SELECT     = (By.ID,            "medicine")
    MEDICINE_NAME       = (By.NAME,          "medicine")
    PACKING_INPUT       = (By.ID,            "packing")
    PACKING_NAME        = (By.NAME,          "packing")
    SAVE_BTN            = (By.ID,            "submit")

    # DataTable
    TABLE               = (By.ID,            "medicine_details")
    TABLE_WRAPPER       = (By.ID,            "medicine_details_wrapper")
    SEARCH_INPUT        = (By.CSS_SELECTOR,  "#medicine_details_filter input")
    PAGE_INFO           = (By.ID,            "medicine_details_info")
    PAGINATE            = (By.ID,            "medicine_details_paginate")
    PREV_BTN            = (By.ID,            "medicine_details_previous")
    NEXT_BTN            = (By.ID,            "medicine_details_next")

    ANY_EDIT_BTN        = (By.CSS_SELECTOR,  "#medicine_details tbody tr:first-child td:last-child a")


# =============================================================================
# REPORTS PAGE  (reports.php)
# =============================================================================
class ReportsPage:
    PAGE_HEADING            = (By.CSS_SELECTOR,  "section.content-header h1")

    # Section 1 — Patient Visits Report
    VISITS_HEADING          = (By.XPATH,         "//h3[text()='Patient Visits Between Two Dates']")
    PATIENTS_FROM           = (By.ID,            "patients_from")
    PATIENTS_FROM_NAME      = (By.NAME,          "patients_from")
    PATIENTS_TO             = (By.ID,            "patients_to")
    PATIENTS_TO_NAME        = (By.NAME,          "patients_to")
    GENERATE_VISITS_PDF     = (By.ID,            "print_visits")

    # Section 2 — Disease Based Report
    DISEASE_HEADING         = (By.XPATH,         "//h3[text()='Disease Based Report Between Two Dates']")
    DISEASE_INPUT           = (By.ID,            "disease")
    DISEASE_FROM            = (By.ID,            "disease_from")
    DISEASE_FROM_NAME       = (By.NAME,          "disease_from")
    DISEASE_TO              = (By.ID,            "disease_to")
    DISEASE_TO_NAME         = (By.NAME,          "disease_to")
    GENERATE_DISEASE_PDF    = (By.ID,            "print_diseases")


# =============================================================================
# USERS PAGE  (users.php)
# =============================================================================
class UsersPage:
    PAGE_HEADING        = (By.CSS_SELECTOR,  "section.content-header h1")
    FORM_HEADING        = (By.XPATH,         "//h3[text()='Add User']")
    TABLE_HEADING       = (By.XPATH,         "//h3[text()='All Users']")

    # Form
    DISPLAY_NAME        = (By.ID,            "display_name")
    DISPLAY_NAME_NAME   = (By.NAME,          "display_name")
    USERNAME            = (By.ID,            "user_name")
    USERNAME_NAME       = (By.NAME,          "user_name")
    PASSWORD            = (By.ID,            "password")
    PASSWORD_NAME       = (By.NAME,          "password")
    PROFILE_PIC         = (By.ID,            "profile_picture")
    SAVE_BTN            = (By.NAME,          "save_user")
    SAVE_BTN_ID         = (By.ID,            "save_medicine")   # shares id with medicine save

    # Table
    TABLE               = (By.ID,            "all_users")
    ANY_EDIT_BTN        = (By.CSS_SELECTOR,  "#all_users tbody tr:first-child td:last-child a")
