import streamlit as st
import numpy as np
import joblib
import os
import time

# Page Configuration
st.set_page_config(page_title="Pre-Auth Fraud Shield", layout="wide", page_icon="🛑")

st.title("🛑 Pre-Authorization Fraud Prevention Engine")
st.markdown("### Active Payment Gateway Intercept System")
st.write("This engine intercepts incoming transaction payloads *before authorization* to evaluate multidimensional risk vectors and enforce live structural blocks.")

st.markdown("---")

# File paths for model artifacts
MODEL_PATH = "models/xgboost_model.pkl"
SCALER_PATH = "models/scaler.pkl"

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    # Load models
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    
    st.subheader("📥 Incoming Gateway Payload Stream")
    
    # 3-Column Layout for comprehensive telemetry
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 💵 Financial Metrics")
        amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=75.0, step=5.0)
        velocity_10m = st.slider("Attempts on Card (Past 10 Mins)", min_value=1, max_value=15, value=1)
        cvv_failures = st.selectbox("CVV/Expiry Match Attempts", ["0 (First Match)", "1 Failure", "2 Failures", "3+ Sequential Failures"])

    with col2:
        st.markdown("#### 🌐 Network & Device Telemetry")
        location_risk = st.selectbox(
            "Geographic / Location Telemetry",
            ["Low Risk (Verified Home Base)", "Medium Risk (Out-of-State Travel)", "High Risk (Sudden Cross-Border Jump)"]
        )
        network_type = st.selectbox(
            "Connection Subnet Routing",
            ["Residential ISP (Clean IP)", "Public Wi-Fi (Unsecured Router)", "Commercial Proxy / Bulletproof VPN Node"]
        )
        device_history = st.selectbox(
            "Device Fingerprint Record",
            ["Trusted (Recognized Hardware GUID)", "New Device (First Login Profile)", "Flagged Device (Associated with prior chargebacks)"]
        )

    with col3:
        st.markdown("#### 🧠 Behavioral & Merchant Profiling")
        behavior_anomaly = st.selectbox(
            "User Navigation Velocity",
            ["Normal (Human typing cadence & reading delays)", "Suspicious (Instant form-fill / Bot scripts detected)"]
        )
        address_match = st.selectbox(
            "Billing vs. Shipping Address Match",
            ["Exact Match", "Country Match / Street Mismatch", "Severe Cross-Border Conflict (US Card -> Shipping to High-Risk Zone)"]
        )
        merchant_trust = st.selectbox(
            "Merchant Terminal Credential",
            ["High Trust Whitelist", "Standard Retail Node", "Unverified Peer-to-Peer Node / Newly Registered Domain"]
        )

    st.markdown("---")
    
    if st.button("⚡ Process Real-Time Pre-Auth Check", type="primary"):
        
        # UI Processing Animation to simulate a real payment gateway check
        with st.status("🔬 Intercepting gateway payload... running risk checks...", expanded=True) as status:
            time.sleep(0.6)
            
            # ==========================================
            # STEP 1: PRE-AUTH HARD FIREWALL RULES (Deterministic)
            # ==========================================
            status.update(label="Checking deterministic firewall rules...", state="running")
            time.sleep(0.4)
            
            hard_block = False
            block_reason = ""
            
            if velocity_10m >= 6:
                hard_block = True
                block_reason = "EXCESSIVE VELOCITY: Card velocity exceeded threshold limit (6+ attempts within a 10-minute window)."
            elif cvv_failures == "3+ Sequential Failures":
                hard_block = True
                block_reason = "BRUTE FORCE DETECTED: Multiple sequential CVV/Expiration mismatches observed."
            elif address_match == "Severe Cross-Border Conflict (US Card -> Shipping to High-Risk Zone)" and network_type == "Commercial Proxy / Bulletproof VPN Node":
                hard_block = True
                block_reason = "GEO-ROUTING FRAUD: Extreme structural conflict between card origin, network location, and shipping endpoint."

            # ==========================================
            # STEP 2: MACHINE LEARNING TRANSLATION LAYER
            # ==========================================
            status.update(label="Compiling multi-vector telemetry into AI model...", state="running")
            
            # Reset baseline vector
            v_inputs = [0.0] * 28
            
            # To fix your issue: We distribute weights across ALL heavy-hitting fraud components 
            # (V14, V12, V10, V17 drop hard for fraud; V4, V11 spike up for fraud)
            
            # Apply signals based on ALL user selections, not just location
            if "High Risk" in location_risk:
                v_inputs[11] -= 4.0  # V12
                v_inputs[13] -= 4.0  # V14
            elif "Medium Risk" in location_risk:
                v_inputs[11] -= 1.5
                
            if "VPN Node" in network_type:
                v_inputs[9] -= 4.5   # V10
                v_inputs[3] += 3.5   # V4
            
            if "Flagged Device" in device_history:
                v_inputs[16] -= 4.0  # V17
                v_inputs[11] -= 2.0  # V12
                
            if "Bot scripts" in behavior_anomaly:
                v_inputs[1] -= 3.0   # V2
                v_inputs[3] += 3.0   # V4
                
            if "Severe Cross-Border" in address_match:
                v_inputs[13] -= 3.5  # V14
                v_inputs[10] += 3.5  # V11
                
            if "Unverified" in merchant_trust:
                v_inputs[6] -= 3.5   # V7
                v_inputs[10] += 2.5  # V11

            # Assemble complete feature string [V1-V28, Amount]
            final_features = np.array(v_inputs + [amount]).reshape(1, -1)
            scaled_features = scaler.transform(final_features)
            
            # Model inference
            ml_prediction = model.predict(scaled_features)[0]
            probabilities = model.predict_proba(scaled_features)[0]
            fraud_probability = probabilities[1] * 100
            
            time.sleep(0.4)
            status.update(label="Inference complete. Enforcing decision pipeline...", state="complete")

        # ==========================================
        # STEP 3: DUAL-ENGINE ENFORCEMENT OUTPUT
        # ==========================================
        st.markdown("### 📋 Gateway Policy Action Decision")
        
        # Scenario A: Blocked by Hard Security Rules
        if hard_block:
            st.error(f"❌ **TRANSACTION TERMINATED (HARD FIREWALL OVERRIDE)**\n\n"
                     f"**Action:** Captured payload dropped before clearing.\n\n"
                     f"**Reason:** {block_reason}\n\n"
                     f"**AI Risk Correlation Score:** {fraud_probability:.2f}% risk matching profile.")
            st.toast("Security Threat Deflected!", icon="🛑")
            
        # Scenario B: Blocked by Machine Learning Predictive Threshold
        elif ml_prediction == 1 or fraud_probability > 50.0:
            st.error(f"❌ **TRANSACTION BLOCKED (PREDICTIVE ENGINE CAPTURE)**\n\n"
                     f"**Action:** Pre-auth clearance denied. Funding source hold applied.\n\n"
                     f"**Confidence Matrix:** System calculated a **{fraud_probability:.2f}%** risk match with verified fraud archetypes.\n\n"
                     f"**Anomalous Flags Triggered:** Multi-vector signal misalignment across combined device, behavioral, and structural variables.")
            st.toast("Fraud Subnet Blocked", icon="🚨")
            
        # Scenario C: Clean Transaction Approved
        else:
            st.success(f"✅ **TRANSACTION AUTHORIZED SUCCESSFULY**\n\n"
                       f"**Action:** Pipeline cleared. Payload forwarded securely to the payment network.\n\n"
                       f"**System Metrics:** Integrity matched at **{probabilities[0]*100:.2f}%** safety confidence level.")
            st.toast("Transaction Approved", icon="💳")

else:
    st.info("📊 Operational artifacts missing. Ensure that your model files (`scaler.pkl` and `xgboost_model.pkl`) are fully compiled inside the `models/` directory.")