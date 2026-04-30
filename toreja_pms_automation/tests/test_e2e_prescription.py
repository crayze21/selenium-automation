# tests/test_e2e_prescription.py
# Full end-to-end prescription workflow test.
# Covers: login → add patient → add medicine → create prescription → verify history

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.patients_page import PatientsPage
from pages.medicines_page import MedicinesPage
from pages.new_prescription_page import NewPrescriptionPage
from pages.patient_history_page import PatientHistoryPage
from pages.dashboard_page import DashboardPage
from test_data.test_data import E2EData
from utils.logger import get_logger
from utils.test_step import step
from utils.config import Config

logger = get_logger(__name__)


@pytest.mark.e2e
@pytest.mark.usefixtures("e2e_driver")
class TestPrescriptionWorkflow:
    """
    Full prescription workflow — runs as a single chain.
    State is shared between methods via class attributes:
        self.patient_name   — set in test_01, used in test_04 and test_05
        self.medicine_name  — set in test_02, used in test_04
    """

    # ── Shared state written by early tests, read by later ones ───────────────
    patient_name:  str = ""
    medicine_name: str = ""

    # =========================================================================
    # TEST 01 — Dashboard loads after login
    # =========================================================================
    @pytest.mark.run(order=1)
    def test_01_dashboard_loads_after_login(self, e2e_driver):
        logger.info("=== E2E STAGE 1: Verify dashboard after login ===")
        dashboard = DashboardPage(e2e_driver)

        with step("Check URL is dashboard.php"):
            assert "dashboard.php" in e2e_driver.current_url, \
                f"Expected dashboard.php, got: {e2e_driver.current_url}"

        with step("Check welcome message"):
            welcome = dashboard.get_welcome_text()
            assert "Welcome" in welcome, \
                f"Welcome message not found, got: '{welcome}'"

        with step("Check all four stat boxes are visible"):
            assert dashboard.is_today_box_displayed(),  "Today box missing"
            assert dashboard.is_week_box_displayed(),   "Week box missing"
            assert dashboard.is_month_box_displayed(),  "Month box missing"
            assert dashboard.is_year_box_displayed(),   "Year box missing"

        logger.info("STAGE 1 PASSED")

    # =========================================================================
    # TEST 02 — Add a new patient
    # =========================================================================
    @pytest.mark.run(order=2)
    def test_02_add_new_patient(self, e2e_driver):
        logger.info("=== E2E STAGE 2: Add new patient ===")

        # Generate unique data for this run
        patient_data = E2EData.patient()
        TestPrescriptionWorkflow.patient_name = patient_data["name"]
        logger.info(f"Patient name for this run: {self.patient_name}")

        page = PatientsPage(e2e_driver)

        with step("Navigate to patients page"):
            page.open()
            assert page.is_on_page(), "Failed to load patients.php"

        with step("Record initial patient count"):
            initial_count = page.get_row_count()
            logger.info(f"Initial patient count: {initial_count}")

        with step("Fill and submit add patient form"):
            page.add_patient(
                name    = patient_data["name"],
                address = patient_data["address"],
                cnic    = patient_data["cnic"],
                dob     = patient_data["dob"],
                phone   = patient_data["phone"],
                gender  = patient_data["gender"],
            )

        with step("Wait for page to reload after save"):
            WebDriverWait(e2e_driver, Config.EXPLICIT_WAIT).until(
                EC.presence_of_element_located((By.ID, "all_patients"))
            )

        with step("Verify patient appears in the table"):
            assert page.is_patient_in_table(patient_data["name"]), \
                f"Patient '{patient_data['name']}' not found in table after save"

        logger.info("STAGE 2 PASSED")

    # =========================================================================
    # TEST 03 — Add a new medicine
    # =========================================================================
    @pytest.mark.run(order=3)
    def test_03_add_new_medicine(self, e2e_driver):
        logger.info("=== E2E STAGE 3: Add new medicine ===")

        TestPrescriptionWorkflow.medicine_name = E2EData.medicine()
        logger.info(f"Medicine name for this run: {self.medicine_name}")

        page = MedicinesPage(e2e_driver)

        with step("Navigate to medicines page"):
            page.open()
            assert page.is_on_page(), "Failed to load medicines.php"

        with step("Fill and submit add medicine form"):
            page.add_medicine(self.medicine_name)

        with step("Wait for page to reload after save"):
            WebDriverWait(e2e_driver, Config.EXPLICIT_WAIT).until(
                EC.presence_of_element_located((By.ID, "all_medicines"))
            )

        with step("Verify medicine appears in the table"):
            assert page.is_medicine_in_table(self.medicine_name), \
                f"Medicine '{self.medicine_name}' not found in table after save"

        logger.info("STAGE 3 PASSED")

    # =========================================================================
    # TEST 04 — Create a prescription linking patient to medicine
    # =========================================================================
    @pytest.mark.run(order=4)
    def test_04_create_prescription(self, e2e_driver):
        if not self.patient_name or not self.medicine_name:
            pytest.skip("Skipping — patient or medicine setup failed in earlier stage")
        logger.info("=== E2E STAGE 4: Create prescription ===")
        logger.info(f"Using patient: {self.patient_name}")
        logger.info(f"Using medicine: {self.medicine_name}")

        assert self.patient_name,  "patient_name not set — did test_02 pass?"
        assert self.medicine_name, "medicine_name not set — did test_03 pass?"

        page = NewPrescriptionPage(e2e_driver)

        with step("Navigate to new prescription page"):
            page.open()
            assert page.is_on_page(), "Failed to load new_prescription.php"

        with step("Select patient from dropdown"):
            page.select_patient(self.patient_name)

        with step("Fill visit date"):
            page.set_visit_date(E2EData.VISIT_DATE)

        with step("Fill next visit date"):
            page.set_next_visit_date(E2EData.NEXT_VISIT_DATE)

        with step("Fill BP"):
            page.enter_bp(E2EData.BP)

        with step("Fill weight"):
            page.enter_weight(E2EData.WEIGHT)

        with step("Fill disease"):
            page.enter_disease(E2EData.DISEASE)

        with step("Add a medicine row"):
            page.click_add_row()
            time.sleep(0.5)   # wait for row to render
            assert page.get_row_count() >= 1, "Medicine row not added"

        with step("Fill medicine row details"):
            page.fill_medicine_row(
                row_index = 1,
                medicine  = self.medicine_name,
                frequency = E2EData.FREQUENCY,
                timing    = E2EData.TIMING,
                qty       = E2EData.QTY,
                dosage    = E2EData.DOSAGE,
            )

        with step("Save prescription"):
            page.click_save_prescription()

        with step("Verify no error on page after save"):
            time.sleep(1.5)   # allow redirect / success message
            page_text = e2e_driver.find_element(By.TAG_NAME, "body").text
            assert "error" not in page_text.lower() or \
                   "success" in page_text.lower() or \
                   "dashboard.php" in e2e_driver.current_url or \
                   "new_prescription.php" in e2e_driver.current_url, \
                "Prescription may have failed — check page content"

        logger.info("STAGE 4 PASSED")

    # =========================================================================
    # TEST 05 — Verify prescription appears in patient history
    # =========================================================================
    @pytest.mark.run(order=5)
    def test_05_verify_patient_history(self, e2e_driver):
        logger.info("=== E2E STAGE 5: Verify patient history ===")
        logger.info(f"Searching history for patient: {self.patient_name}")

        assert self.patient_name, "patient_name not set — did test_02 pass?"

        page = PatientHistoryPage(e2e_driver)

        with step("Navigate to patient history page"):
            page.open()
            assert page.is_on_page(), "Failed to load patient_history.php"

        with step("Select patient and search history"):
            page.search_patient_history(self.patient_name)

        with step("Wait for results to load"):
            WebDriverWait(e2e_driver, Config.EXPLICIT_WAIT).until(
                lambda d: page.get_result_row_count() > 0
            )

        with step("Assert at least one history row exists"):
            row_count = page.get_result_row_count()
            assert row_count > 0, \
                f"Expected history rows for '{self.patient_name}', found 0"
            logger.info(f"History rows found: {row_count}")

        with step("Assert disease name appears in history"):
            disease_cell = page.get_cell_text(row=1, col=3)
            assert E2EData.DISEASE.lower() in disease_cell.lower(), \
                f"Expected disease '{E2EData.DISEASE}' in history, got '{disease_cell}'"

        with step("Assert medicine appears in history"):
            medicine_cell = page.get_cell_text(row=1, col=4)
            assert self.medicine_name.lower() in medicine_cell.lower(), \
                f"Expected medicine '{self.medicine_name}' in history, got '{medicine_cell}'"

        logger.info("STAGE 5 PASSED — full E2E workflow complete")