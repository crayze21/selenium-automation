# =============================================================================
# TOREJA MEDICAL CLINIC - PATIENT MANAGEMENT SYSTEM
# Complete Selenium Locators
# URL: http://torejamedicalclinic.wuaze.com
# =============================================================================
# Locator format:  (By.STRATEGY, "value")
# Strategies used: By.ID, By.NAME, By.CSS_SELECTOR, By.XPATH, By.LINK_TEXT
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
# PAGE: LOGIN  (index.php)
# =============================================================================
class LoginPage:
    # ── Branding ──────────────────────────────────────────────────────────────
    LOGO            = (By.ID,          "system-logo")
    PAGE_TITLE_TEXT = (By.CSS_SELECTOR, "h4")               # "Toreja Medical Clinic - Patient Management System"

    # ── Form fields ───────────────────────────────────────────────────────────
    USERNAME_INPUT      = (By.ID,   "user_name")
    USERNAME_INPUT_NAME = (By.NAME, "user_name")
    PASSWORD_INPUT      = (By.ID,   "password")
    PASSWORD_INPUT_NAME = (By.NAME, "password")

    # ── Buttons ───────────────────────────────────────────────────────────────
    LOGIN_BUTTON      = (By.NAME,        "login")
    LOGIN_BUTTON_XPATH = (By.XPATH,      "//button[@name='login']")
    LOGIN_BUTTON_CSS   = (By.CSS_SELECTOR, "button[name='login']")

    # ── Messages ──────────────────────────────────────────────────────────────
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p")                  # "Incorrect username or password."
    SUBTITLE_TEXT = (By.XPATH, "//p[contains(text(),'Please enter your login credentials')]")


# =============================================================================
# SHARED: NAVIGATION BAR  (present on all authenticated pages)
# =============================================================================
class NavBar:
    # ── Top bar ───────────────────────────────────────────────────────────────
    NAV_BAR            = (By.CSS_SELECTOR, "nav.main-header")
    TOGGLE_SIDEBAR_BTN = (By.CSS_SELECTOR, "a[data-widget='pushmenu']")
    BRAND_LINK         = (By.CSS_SELECTOR, "a.navbar-brand")
    BRAND_TEXT         = (By.CSS_SELECTOR, "span.brand-text")
    WELCOME_TEXT       = (By.CSS_SELECTOR, "div.login-user")  # "Welcome, Administrator!"

    # ── Sidebar ───────────────────────────────────────────────────────────────
    SIDEBAR            = (By.CSS_SELECTOR, "aside.main-sidebar")
    SIDEBAR_BRAND_LINK = (By.CSS_SELECTOR, "a.brand-link.logo-switch")
    SIDEBAR_LOGO_XS    = (By.CSS_SELECTOR, "h4.logo-xs")
    SIDEBAR_LOGO_XL    = (By.CSS_SELECTOR, "h4.logo-xl")
    USER_AVATAR        = (By.CSS_SELECTOR, "div.user-panel img.img-circle")
    USER_PANEL_NAME    = (By.CSS_SELECTOR, "div.user-panel div.info a")

    # ── Sidebar menu items (nav links) ────────────────────────────────────────
    MENU_DASHBOARD       = (By.ID, "mnu_dashboard")
    MENU_DASHBOARD_LINK  = (By.CSS_SELECTOR, "#mnu_dashboard > a")
    MENU_PATIENTS        = (By.ID, "mnu_patients")
    MENU_PATIENTS_LINK   = (By.CSS_SELECTOR, "#mnu_patients > a")
    MENU_MEDICINES       = (By.ID, "mnu_medicines")
    MENU_MEDICINES_LINK  = (By.CSS_SELECTOR, "#mnu_medicines > a")
    MENU_REPORTS         = (By.ID, "mnu_reports")
    MENU_REPORTS_LINK    = (By.CSS_SELECTOR, "#mnu_reports > a")
    MENU_USERS           = (By.ID, "mnu_users")
    MENU_USERS_LINK      = (By.CSS_SELECTOR, "#mnu_users > a")

    # ── Sidebar sub-menu items ────────────────────────────────────────────────
    SUBMENU_NEW_PRESCRIPTION  = (By.ID, "mi_new_prescription")
    SUBMENU_PATIENTS          = (By.ID, "mi_patients")
    SUBMENU_PATIENT_HISTORY   = (By.ID, "mi_patient_history")
    SUBMENU_ADD_MEDICINE      = (By.ID, "mi_medicines")
    SUBMENU_MEDICINE_DETAILS  = (By.ID, "mi_medicine_details")
    SUBMENU_REPORTS           = (By.ID, "mi_reports")

    # ── Logout ────────────────────────────────────────────────────────────────
    LOGOUT_LINK     = (By.XPATH,        "//a[@href='logout.php']")
    LOGOUT_LINK_CSS = (By.CSS_SELECTOR, "a[href='logout.php']")

    # ── Footer ────────────────────────────────────────────────────────────────
    FOOTER      = (By.CSS_SELECTOR, "footer.main-footer")
    FOOTER_LINK = (By.CSS_SELECTOR, "footer a[href='dashboard.php']")


# =============================================================================
# PAGE: DASHBOARD  (dashboard.php)
# =============================================================================
class DashboardPage:
    PAGE_HEADING = (By.CSS_SELECTOR, "section.content-header h1")

    # ── Stat boxes ────────────────────────────────────────────────────────────
    STAT_TODAY_PATIENTS = (By.CSS_SELECTOR, "div.small-box.bg-info")
    STAT_CURRENT_WEEK   = (By.CSS_SELECTOR, "div.small-box.bg-purple")
    STAT_CURRENT_MONTH  = (By.CSS_SELECTOR, "div.small-box.bg-fuchsia")
    STAT_CURRENT_YEAR   = (By.CSS_SELECTOR, "div.small-box.bg-maroon")

    STAT_TODAY_COUNT = (By.CSS_SELECTOR, "div.small-box.bg-info h3")
    STAT_WEEK_COUNT  = (By.CSS_SELECTOR, "div.small-box.bg-purple h3")
    STAT_MONTH_COUNT = (By.CSS_SELECTOR, "div.small-box.bg-fuchsia h3")
    STAT_YEAR_COUNT  = (By.CSS_SELECTOR, "div.small-box.bg-maroon h3")

    STAT_TODAY_LABEL = (By.XPATH, "//div[contains(@class,'bg-info')]//p")
    STAT_WEEK_LABEL  = (By.XPATH, "//div[contains(@class,'bg-purple')]//p")
    STAT_MONTH_LABEL = (By.XPATH, "//div[contains(@class,'bg-fuchsia')]//p")
    STAT_YEAR_LABEL  = (By.XPATH, "//div[contains(@class,'bg-maroon')]//p")


# =============================================================================
# PAGE: NEW PRESCRIPTION  (new_prescription.php)
# =============================================================================
class NewPrescriptionPage:
    PAGE_HEADING = (By.CSS_SELECTOR, "section.content-header h1")

    # ── Patient selector (Select2 dropdown) ───────────────────────────────────
    PATIENT_SELECT      = (By.ID,   "patient")
    PATIENT_SELECT_NAME = (By.NAME, "patient[]")
    PATIENT_SEARCH_BOX  = (By.XPATH, "//input[@placeholder='Type Patient Name...']")
    PATIENT_SEARCH_CSS  = (By.CSS_SELECTOR, "input[placeholder='Type Patient Name...']")

    # ── Visit info fields ─────────────────────────────────────────────────────
    VISIT_DATE      = (By.NAME, "visit_date")
    VISIT_DATE_XPATH = (By.XPATH, "//input[@name='visit_date']")
    NEXT_VISIT_DATE = (By.NAME, "next_visit_date")
    BP_INPUT        = (By.NAME, "bp")
    WEIGHT_INPUT    = (By.NAME, "weight")
    DISEASE_INPUT   = (By.NAME, "disease")

    # ── Medicine table ────────────────────────────────────────────────────────
    ADD_ROW_BUTTON    = (By.ID,    "add_row")
    ADD_ROW_BTN_XPATH = (By.XPATH, "//button[@id='add_row']")
    MEDICATION_LIST   = (By.ID,    "medication_list")        # <tbody>

    # ── Medicine row fields (row 1 – repeating pattern) ──────────────────────
    MEDICINE_SELECT     = (By.NAME, "medicine[]")
    MEDICINE_SEARCH_BOX = (By.CSS_SELECTOR, "input[placeholder='Type Medicine...']")
    PACKING_INPUT       = (By.XPATH, "(//input[@name='packing[]'])[1]")
    FREQUENCY_SELECT    = (By.NAME, "frequency[]")
    TIMING_SELECT       = (By.NAME, "timing[]")
    QTY_INPUT           = (By.NAME, "qty[]")
    DOSAGE_INPUT        = (By.NAME, "dosage[]")
    DOSAGE_PLACEHOLDER  = (By.CSS_SELECTOR, "input[placeholder='e.g 500mg']")
    DELETE_ROW_BTN      = (By.XPATH, "(//button[contains(@class,'btn-danger') or @type='button'])[1]")

    # ── Table headers ─────────────────────────────────────────────────────────
    TH_MEDICINE   = (By.XPATH, "//thead//th[1]")
    TH_PACKING    = (By.XPATH, "//thead//th[2]")
    TH_FREQUENCY  = (By.XPATH, "//thead//th[3]")
    TH_TIMING     = (By.XPATH, "//thead//th[4]")
    TH_QTY        = (By.XPATH, "//thead//th[5]")
    TH_DOSAGE     = (By.XPATH, "//thead//th[6]")

    # ── Submit ────────────────────────────────────────────────────────────────
    SAVE_PRESCRIPTION_BTN       = (By.NAME,        "submit")
    SAVE_PRESCRIPTION_BTN_XPATH = (By.XPATH,       "//button[@name='submit']")
    SAVE_PRESCRIPTION_BTN_CSS   = (By.CSS_SELECTOR, "button[name='submit']")


# =============================================================================
# PAGE: PATIENTS  (patients.php)
# =============================================================================
class PatientsPage:
    PAGE_HEADING        = (By.CSS_SELECTOR, "section.content-header h1")
    ADD_PATIENTS_HEADER = (By.XPATH, "//h3[text()='Add Patients']")

    # ── Add Patient form ──────────────────────────────────────────────────────
    PATIENT_NAME_INPUT = (By.ID,   "patient_name")
    PATIENT_NAME_NAME  = (By.NAME, "patient_name")
    ADDRESS_INPUT      = (By.ID,   "address")
    ADDRESS_NAME       = (By.NAME, "address")
    CNIC_INPUT         = (By.ID,   "cnic")
    CNIC_NAME          = (By.NAME, "cnic")
    DATE_OF_BIRTH_DIV  = (By.ID,   "date_of_birth")           # datepicker wrapper
    DATE_OF_BIRTH_INPUT = (By.NAME, "date_of_birth")
    PHONE_NUMBER_INPUT = (By.ID,   "phone_number")
    PHONE_NUMBER_NAME  = (By.NAME, "phone_number")
    GENDER_SELECT      = (By.ID,   "gender")
    GENDER_SELECT_NAME = (By.NAME, "gender")
    SAVE_PATIENT_BTN   = (By.ID,   "save_Patient")
    SAVE_PATIENT_NAME  = (By.NAME, "save_Patient")

    # ── Patient table ─────────────────────────────────────────────────────────
    TABLE_WRAPPER    = (By.ID, "all_patients_wrapper")
    TABLE            = (By.ID, "all_patients")
    TABLE_FILTER_DIV = (By.ID, "all_patients_filter")
    SEARCH_INPUT     = (By.CSS_SELECTOR, "#all_patients_filter input")

    # ── Export buttons ────────────────────────────────────────────────────────
    COPY_BTN          = (By.XPATH, "//button[.//span[text()='Copy']]")
    CSV_BTN           = (By.XPATH, "//button[.//span[text()='CSV']]")
    EXCEL_BTN         = (By.XPATH, "//button[.//span[text()='Excel']]")
    PDF_BTN           = (By.XPATH, "//button[.//span[text()='PDF']]")
    PRINT_BTN         = (By.XPATH, "//button[.//span[text()='Print']]")
    COLUMN_VISIBILITY = (By.XPATH, "//button[.//span[text()='Column visibility']]")

    # ── Table headers ─────────────────────────────────────────────────────────
    TH_SNO          = (By.XPATH, "//table[@id='all_patients']//th[1]")
    TH_PATIENT_NAME = (By.XPATH, "//table[@id='all_patients']//th[2]")
    TH_ADDRESS      = (By.XPATH, "//table[@id='all_patients']//th[3]")
    TH_CNIC         = (By.XPATH, "//table[@id='all_patients']//th[4]")
    TH_DOB          = (By.XPATH, "//table[@id='all_patients']//th[5]")
    TH_PHONE        = (By.XPATH, "//table[@id='all_patients']//th[6]")
    TH_GENDER       = (By.XPATH, "//table[@id='all_patients']//th[7]")
    TH_ACTION       = (By.XPATH, "//table[@id='all_patients']//th[8]")

    # ── Pagination ────────────────────────────────────────────────────────────
    PAGINATION_DIV = (By.ID, "all_patients_paginate")
    PREV_BTN       = (By.ID, "all_patients_previous")
    NEXT_BTN       = (By.ID, "all_patients_next")
    PAGE_INFO      = (By.ID, "all_patients_info")


# =============================================================================
# PAGE: PATIENT HISTORY  (patient_history.php)
# =============================================================================
class PatientHistoryPage:
    PAGE_HEADING    = (By.CSS_SELECTOR, "section.content-header h1")
    SECTION_HEADING = (By.XPATH, "//h3[text()='Search Patient History']")

    # ── Search form ───────────────────────────────────────────────────────────
    PATIENT_SELECT     = (By.ID,  "patient")
    PATIENT_SEARCH_BOX = (By.CSS_SELECTOR, "input[placeholder='Type Patient Name...']")
    SEARCH_BTN         = (By.ID,  "search")
    SEARCH_BTN_XPATH   = (By.XPATH, "//button[@id='search']")

    # ── Results table ─────────────────────────────────────────────────────────
    TABLE        = (By.ID, "patient_history")
    HISTORY_BODY = (By.ID, "history_data")

    TH_SNO        = (By.XPATH, "//table[@id='patient_history']//th[1]")
    TH_VISIT_DATE = (By.XPATH, "//table[@id='patient_history']//th[2]")
    TH_DISEASE    = (By.XPATH, "//table[@id='patient_history']//th[3]")
    TH_MEDICINE   = (By.XPATH, "//table[@id='patient_history']//th[4]")
    TH_PACKING    = (By.XPATH, "//table[@id='patient_history']//th[5]")
    TH_QTY        = (By.XPATH, "//table[@id='patient_history']//th[6]")
    TH_DOSAGE     = (By.XPATH, "//table[@id='patient_history']//th[7]")
    TH_INSTRUCTION = (By.XPATH, "//table[@id='patient_history']//th[8]")
    TH_ACTION     = (By.XPATH, "//table[@id='patient_history']//th[9]")


# =============================================================================
# PAGE: MEDICINES  (medicines.php)
# =============================================================================
class MedicinesPage:
    PAGE_HEADING        = (By.CSS_SELECTOR, "section.content-header h1")
    ADD_MEDICINE_HEADER = (By.XPATH, "//h3[text()='Add Medicine']")

    # ── Add Medicine form ─────────────────────────────────────────────────────
    MEDICINE_NAME_INPUT = (By.ID,   "medicine_name")
    MEDICINE_NAME_NAME  = (By.NAME, "medicine_name")
    SAVE_MEDICINE_BTN   = (By.ID,   "save_medicine")
    SAVE_MEDICINE_NAME  = (By.NAME, "save_medicine")

    # ── Medicines table ───────────────────────────────────────────────────────
    TABLE_WRAPPER    = (By.ID, "all_medicines_wrapper")
    TABLE            = (By.ID, "all_medicines")
    TABLE_FILTER_DIV = (By.ID, "all_medicines_filter")
    SEARCH_INPUT     = (By.CSS_SELECTOR, "#all_medicines_filter input")

    # ── Export buttons ────────────────────────────────────────────────────────
    COPY_BTN          = (By.XPATH, "//button[.//span[text()='Copy']]")
    CSV_BTN           = (By.XPATH, "//button[.//span[text()='CSV']]")
    EXCEL_BTN         = (By.XPATH, "//button[.//span[text()='Excel']]")
    PDF_BTN           = (By.XPATH, "//button[.//span[text()='PDF']]")
    PRINT_BTN         = (By.XPATH, "//button[.//span[text()='Print']]")
    COLUMN_VISIBILITY = (By.XPATH, "//button[.//span[text()='Column visibility']]")

    # ── Table headers ─────────────────────────────────────────────────────────
    TH_SNO          = (By.XPATH, "//table[@id='all_medicines']//th[1]")
    TH_MEDICINE_NAME = (By.XPATH, "//table[@id='all_medicines']//th[2]")
    TH_ACTION       = (By.XPATH, "//table[@id='all_medicines']//th[3]")

    # ── Pagination ────────────────────────────────────────────────────────────
    PAGINATION_DIV = (By.ID, "all_medicines_paginate")
    PREV_BTN       = (By.ID, "all_medicines_previous")
    NEXT_BTN       = (By.ID, "all_medicines_next")
    PAGE_INFO      = (By.ID, "all_medicines_info")


# =============================================================================
# PAGE: MEDICINE DETAILS  (medicine_details.php)
# =============================================================================
class MedicineDetailsPage:
    PAGE_HEADING       = (By.CSS_SELECTOR, "section.content-header h1")
    ADD_DETAILS_HEADER = (By.XPATH, "//h3[text()='Add Medicine Details']")

    # ── Add Medicine Details form ─────────────────────────────────────────────
    MEDICINE_SELECT      = (By.ID,   "medicine")
    MEDICINE_SELECT_NAME = (By.NAME, "medicine")
    PACKING_INPUT        = (By.ID,   "packing")
    PACKING_INPUT_NAME   = (By.NAME, "packing")
    SAVE_BTN             = (By.ID,   "submit")
    SAVE_BTN_NAME        = (By.NAME, "submit")

    # ── Medicine Details table ────────────────────────────────────────────────
    TABLE_WRAPPER    = (By.ID, "medicine_details_wrapper")
    TABLE            = (By.ID, "medicine_details")
    TABLE_FILTER_DIV = (By.ID, "medicine_details_filter")
    SEARCH_INPUT     = (By.CSS_SELECTOR, "#medicine_details_filter input")

    # ── Export buttons ────────────────────────────────────────────────────────
    COPY_BTN          = (By.XPATH, "//button[.//span[text()='Copy']]")
    CSV_BTN           = (By.XPATH, "//button[.//span[text()='CSV']]")
    EXCEL_BTN         = (By.XPATH, "//button[.//span[text()='Excel']]")
    PDF_BTN           = (By.XPATH, "//button[.//span[text()='PDF']]")
    PRINT_BTN         = (By.XPATH, "//button[.//span[text()='Print']]")
    COLUMN_VISIBILITY = (By.XPATH, "//button[.//span[text()='Column visibility']]")

    # ── Table headers ─────────────────────────────────────────────────────────
    TH_SNO          = (By.XPATH, "//table[@id='medicine_details']//th[1]")
    TH_MEDICINE_NAME = (By.XPATH, "//table[@id='medicine_details']//th[2]")
    TH_PACKING      = (By.XPATH, "//table[@id='medicine_details']//th[3]")
    TH_ACTION       = (By.XPATH, "//table[@id='medicine_details']//th[4]")

    # ── Pagination ────────────────────────────────────────────────────────────
    PAGINATION_DIV = (By.ID, "medicine_details_paginate")
    PREV_BTN       = (By.ID, "medicine_details_previous")
    NEXT_BTN       = (By.ID, "medicine_details_next")
    PAGE_INFO      = (By.ID, "medicine_details_info")


# =============================================================================
# PAGE: REPORTS  (reports.php)
# =============================================================================
class ReportsPage:
    PAGE_HEADING = (By.CSS_SELECTOR, "section.content-header h1")

    # ── Section 1 – Patient Visits Report ─────────────────────────────────────
    VISITS_SECTION_HEADER         = (By.XPATH, "//h3[text()='Patient Visits Between Two Dates']")
    PATIENTS_FROM_INPUT           = (By.ID,   "patients_from")
    PATIENTS_FROM_NAME            = (By.NAME, "patients_from")
    PATIENTS_TO_INPUT             = (By.ID,   "patients_to")
    PATIENTS_TO_NAME              = (By.NAME, "patients_to")
    GENERATE_VISITS_PDF_BTN       = (By.ID,   "print_visits")
    GENERATE_VISITS_PDF_BTN_XPATH = (By.XPATH, "//button[@id='print_visits']")

    # ── Section 2 – Disease Based Report ──────────────────────────────────────
    DISEASE_SECTION_HEADER          = (By.XPATH, "//h3[text()='Disease Based Report Between Two Dates']")
    DISEASE_INPUT                   = (By.ID,   "disease")
    DISEASE_FROM_INPUT              = (By.ID,   "disease_from")
    DISEASE_FROM_NAME               = (By.NAME, "disease_from")
    DISEASE_TO_INPUT                = (By.ID,   "disease_to")
    DISEASE_TO_NAME                 = (By.NAME, "disease_to")
    GENERATE_DISEASE_PDF_BTN        = (By.ID,   "print_diseases")
    GENERATE_DISEASE_PDF_BTN_XPATH  = (By.XPATH, "//button[@id='print_diseases']")


# =============================================================================
# PAGE: USERS  (users.php)
# =============================================================================
class UsersPage:
    PAGE_HEADING     = (By.CSS_SELECTOR, "section.content-header h1")
    ADD_USER_HEADER  = (By.XPATH, "//h3[text()='Add User']")
    ALL_USERS_HEADER = (By.XPATH, "//h3[text()='All Users']")

    # ── Add User form ─────────────────────────────────────────────────────────
    DISPLAY_NAME_INPUT = (By.ID,   "display_name")
    DISPLAY_NAME_NAME  = (By.NAME, "display_name")
    USERNAME_INPUT     = (By.ID,   "user_name")
    USERNAME_NAME      = (By.NAME, "user_name")
    PASSWORD_INPUT     = (By.ID,   "password")
    PASSWORD_NAME      = (By.NAME, "password")
    PROFILE_PIC_INPUT  = (By.ID,   "profile_picture")
    PROFILE_PIC_NAME   = (By.NAME, "profile_picture")
    SAVE_USER_BTN      = (By.ID,   "save_medicine")           # note: shares same id as medicine save
    SAVE_USER_NAME     = (By.NAME, "save_user")

    # ── Users table ───────────────────────────────────────────────────────────
    TABLE = (By.ID, "all_users")

    TH_SNO          = (By.XPATH, "//table[@id='all_users']//th[1]")
    TH_PICTURE      = (By.XPATH, "//table[@id='all_users']//th[2]")
    TH_DISPLAY_NAME = (By.XPATH, "//table[@id='all_users']//th[3]")
    TH_USERNAME     = (By.XPATH, "//table[@id='all_users']//th[4]")
    TH_ACTION       = (By.XPATH, "//table[@id='all_users']//th[5]")