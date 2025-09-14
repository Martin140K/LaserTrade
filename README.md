# LaserTrade

LaserTrade – Machine Learning predikce cen trhu.


Projekt vznikl pro trénink ML na finančních datech. Cílem není dokonalá predikce, ale pochopení pipeline.


Použité technologie
Python, Pandas, Scikit-learn, Matplotlib, yfinance, Streamlit


Jak spustit
pip install -r requirements.txt
streamlit run app.py


Aplikace
vyplníte ticker(burzovní zkratku) do příslušného pole a stiskněte enter

Výsledky
po 5-10 sekundách se objeví graf s historickými daty trhu a predikce na zítřek, zda půjde nahoru či dolů
na obrazovce uvidíte nejen cenu, ale i indikátory, kterými se řídí obchodníci



Model zachycuje historická data, ale jeho přesnost s sebou nese limity