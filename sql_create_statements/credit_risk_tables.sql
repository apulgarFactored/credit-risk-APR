CREATE TABLE credit_risk_apr.credit_card_balance (
	sk_id_prev BIGINT,
	sk_id_curr BIGINT,
	months_balance BIGINT,
	amt_balance DECIMAL,
	amt_credit_limit_actual BIGINT,
	amt_drawings_atm_current DECIMAL,
	amt_drawings_current DECIMAL,
	amt_drawings_other_current DECIMAL,
	amt_drawings_pos_current DECIMAL,
	amt_inst_min_regularity DECIMAL,
	amt_payment_current DECIMAL,
	amt_payment_total_current DECIMAL,
	amt_receivable_principal DECIMAL,
	amt_recivable DECIMAL,
	amt_total_receivable DECIMAL,
	cnt_drawings_atm_current DECIMAL,
	cnt_drawings_current BIGINT,
	cnt_drawings_other_current DECIMAL,
	cnt_drawings_pos_current DECIMAL,
	cnt_instalment_mature_cum DECIMAL,
	name_contract_status VARCHAR(100),
	sk_dpd BIGINT,
	sk_dpd_def BIGINT
);


CREATE TABLE credit_risk_apr.installments_payments (
	sk_id_prev BIGINT,
	sk_id_curr BIGINT,
	num_instalment_version DECIMAL,
	num_instalment_number BIGINT,
	days_instalment DECIMAL,
	days_entry_payment DECIMAL,
	amt_instalment DECIMAL,
	amt_payment DECIMAL
);


CREATE TABLE credit_risk_apr.pos_cash_balance (
	sk_id_prev BIGINT,
	sk_id_curr BIGINT,
	months_balance BIGINT,
	cnt_instalment DECIMAL,
	cnt_instalment_future DECIMAL,
	name_contract_status VARCHAR(100),
	sk_dpd BIGINT,
	sk_dpd_def BIGINT
);


CREATE TABLE credit_risk_apr.bureau_balance (
	sk_id_bureau BIGINT,
	months_balance BIGINT,
	status VARCHAR(100)
);


CREATE TABLE credit_risk_apr.bureau (
	sk_id_curr BIGINT,
	sk_id_bureau BIGINT,
	credit_active VARCHAR(100),
	credit_currency VARCHAR(100),
	days_credit BIGINT,
	credit_day_overdue BIGINT,
	days_credit_enddate DECIMAL,
	days_enddate_fact DECIMAL,
	amt_credit_max_overdue DECIMAL,
	cnt_credit_prolong BIGINT,
	amt_credit_sum DECIMAL,
	amt_credit_sum_debt DECIMAL,
	amt_credit_sum_limit DECIMAL,
	amt_credit_sum_overdue DECIMAL,
	credit_type VARCHAR(100),
	days_credit_update BIGINT,
	amt_annuity DECIMAL
);


CREATE TABLE credit_risk_apr.previous_application(
	sk_id_prev BIGINT,
	sk_id_curr BIGINT,
	name_contract_type VARCHAR(100),
	amt_annuity DECIMAL,
	amt_application DECIMAL,
	amt_credit DECIMAL,
	amt_down_payment DECIMAL,
	amt_goods_price DECIMAL,
	weekday_appr_process_start VARCHAR(100),
	hour_appr_process_start BIGINT,
	flag_last_appl_per_contract VARCHAR(100),
	nflag_last_appl_in_day BIGINT,
	rate_down_payment VARCHAR(100),
	rate_interest_primary DECIMAL,
	rate_interest_privileged DECIMAL,
	name_cash_loan_purpose VARCHAR(100),
	name_contract_status VARCHAR(100),
	days_decision BIGINT,
	name_payment_type VARCHAR(100),
	code_reject_reason VARCHAR(100),
	name_type_suite VARCHAR(100),
	name_client_type VARCHAR(100),
	name_goods_category VARCHAR(100),
	name_portfolio VARCHAR(100),
	name_product_type VARCHAR(100),
	channel_type VARCHAR(100),
	sellerplace_area BIGINT,
	name_seller_industry VARCHAR(100),
	cnt_payment DECIMAL,
	name_yield_group VARCHAR(100),
	product_combination VARCHAR(100),
	days_first_drawing DECIMAL,
	days_first_due DECIMAL,
	days_last_due_1st_version DECIMAL,
	days_last_due DECIMAL,
	days_termination DECIMAL,
	nflag_insured_on_approval DECIMAL
);	