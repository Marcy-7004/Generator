import streamlit as st
import stripe

# part1 = "sk_test_51Sq8StQmrQYBzVf1g01x"
part2 = "0E0eyAnLbm6iI7kZHJZCJ0v3mp7URV0qs4gDGm1QJqHoSetSFrPxw9J104opI6N71ecr00v9VCsUCD"
stripe.api_key = part1 + part2

st.set_page_config(page_title="Motivációs Levél Generátor", page_icon="📝")
st.title("🎯 Motivációs Levél Generátor")

st.sidebar.header("💳 Kredit vásárlás")
if st.sidebar.button("10 Kredit vásárlása (3500 Ft)"):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{'price': 'price_1Sq92GQmrQYBzVf1zV296fR5', 'quantity': 1}],
            mode='payment',
            success_url='https://share.streamlit.io/', 
            cancel_url='https://share.streamlit.io/',
        )
        st.sidebar.markdown(f"[👉 KATTINTS IDE A FIZETÉSHEZ]({checkout_session.url})")
    except Exception as e:
        st.sidebar.error(f"Hiba: {e}")

st.subheader("Töltsd ki az adatokat:")
pozicio = st.text_input("Milyen állásra jelentkezel?")
tapasztalat = st.text_area("Írd le pár szóban a tapasztalataidat...")

if st.button("Levél készítése"):
    if pozicio and tapasztalat:
        st.info("A levél generálása folyamatban...")
        szoveg = f"Tisztelt HR Vezető!\n\nEzúton jelentkezem a {pozicio} pozícióra. {tapasztalat} alapján alkalmasnak tartom magam..."
        st.text_area("Elkészült levél:", szoveg, height=250)
    else:
        st.warning("Kérlek, töltsd ki a mezőket!")
