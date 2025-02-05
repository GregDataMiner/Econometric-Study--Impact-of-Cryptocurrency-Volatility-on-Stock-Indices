# 📈 **Econometric Study: Impact of Cryptocurrency Volatility on Stock Indices**

This project explores the influence of cryptocurrency volatility, particularly **Bitcoin** and **Ethereum**, on traditional stock indices like **S&P 500**, **NASDAQ**, and **Dow Jones**. Using advanced econometric models such as **ARCH** and **GARCH**, we analyze the dynamic behavior between these two asset classes over a **4-year period**.

---

## **Project Overview**

### **1. Problem Statement**
- Cryptocurrencies have gained prominence since 2009, altering the financial landscape.
- Their high volatility and complex integration with traditional markets pose new risks and opportunities for investors.

---

### **2. Objectives**
- Examine if cryptocurrency returns can predict stock index performance.
- Test for causality using econometric models.
- Provide insights on how capital shifts between these asset classes during periods of high volatility.

---

### **3. Methodology**
- Import data spanning **4 years**.
- Calculate daily returns for both cryptocurrencies and stock indices.
- Apply **ARCH** and **GARCH** models to capture volatility effects.
- Perform **multiple linear regressions** to study relationships between crypto and stock returns.

```r
# Example R code for GARCH model application
library(rugarch)

spec <- ugarchspec(
    variance.model = list(model = "sGARCH"),
    mean.model = list(armaOrder = c(1, 1))
)
fit <- ugarchfit(spec, data = crypto_returns)
summary(fit)
```

---

### **4. Key Findings**
- **Bitcoin** and **Ethereum** exhibit significant correlations with the NASDAQ index.
- During crypto volatility peaks, capital often shifts toward traditional stock markets, influencing stock prices.
- Cryptocurrencies impact markets differently than traditional macroeconomic factors, making them critical for modern portfolio strategies.

---

### **5. Visuals and Results**
- Descriptive statistics and regression analysis are documented.
- Models illustrate how volatility clusters over time, affecting both crypto and traditional assets.

![Sample Visualization](path/to/your/visual.png)

---

### **6. Conclusion**
- Cryptocurrencies are increasingly integrated into financial markets.
- They offer both risks and opportunities, requiring a balanced approach to investment.
- Understanding their role is essential for future portfolio diversification and risk management.

---

### **7. Resources**
- **Full Report**: Download the complete PDF analysis from this repository.
- **Source Code**: Clone or download the repository to access data and scripts.

For more details, feel free to explore the project files!
