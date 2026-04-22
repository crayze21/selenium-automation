# =============================================================================
# test_data/test_data.py
# Centralised test data used across all test modules
# =============================================================================


class LoginData:
    VALID_USERNAME    = "admin"
    VALID_PASSWORD    = "admin123"
    INVALID_USERNAME  = "wronguser"
    INVALID_PASSWORD  = "wrongpass"
    EMPTY             = ""


class PatientData:
    VALID = {
        "name":    "Test Patient Auto",
        "address": "123 Automation Street, Manila",
        "cnic":    "987654321",
        "dob":     "1995-06-15",
        "phone":   "09123456789",
        "gender":  "Male",
    }
    EXISTING_NAME = "Mark Cooper"   # seeded in the app

    NO_NAME = {
        "name":    "",
        "address": "Some Address",
        "cnic":    "111111111",
        "dob":     "1990-01-01",
        "phone":   "09000000000",
        "gender":  "Female",
    }


class MedicineData:
    VALID_NAME   = "TestMedicineAuto"
    EXISTING     = "Amoxicillin"
    EMPTY_NAME   = ""


class MedicineDetailData:
    MEDICINE = "Losartan"
    PACKING  = "60"


class PrescriptionData:
    PATIENT       = "Mark Cooper"
    VISIT_DATE    = "2026-04-23"
    NEXT_VISIT    = "2026-05-07"
    BP            = "120/80"
    WEIGHT        = "70"
    DISEASE       = "Hypertension"

    MEDICINE      = "Amoxicillin"
    FREQUENCY     = "1-0-1 (M-N)"
    TIMING        = "After Meal"
    QTY           = "10"
    DOSAGE        = "500mg"


class ReportData:
    FROM_DATE     = "2026-01-01"
    TO_DATE       = "2026-12-31"
    DISEASE       = "Hypertension"


class UserData:
    VALID = {
        "display_name": "Auto Test User",
        "username":     "autotestuser",
        "password":     "autotest123",
    }
    EMPTY_USERNAME = {
        "display_name": "No Username",
        "username":     "",
        "password":     "somepass",
    }
    EMPTY_PASSWORD = {
        "display_name": "No Password",
        "username":     "nopwduser",
        "password":     "",
    }
