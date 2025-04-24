document.addEventListener('DOMContentLoaded', function() {
    const toggleButtons = document.querySelectorAll('.toggle-btn');
    const priceAmounts = document.querySelectorAll('.amount');
    const billingInfos = document.querySelectorAll('.billing-info');

    const prices = {
        monthly: {
            basic: 29,
            professional: 49,
            business: 99
        },
        biannual: {
            basic: Math.round(150 / 6),
            professional: Math.round(270 / 6),
            business: Math.round(540 / 6)
        },
        annual: {
            basic: Math.round(264 / 12),
            professional: Math.round(480 / 12),
            business: Math.round(948 / 12)
        }
    };

    const billingText = {
        monthly: 'billed monthly',
        biannual: 'billed every 6 months',
        annual: 'billed annually'
    };

    function updatePrices(duration) {
        const priceList = prices[duration];
        const priceKeys = Object.keys(priceList);
        
        priceAmounts.forEach((amount, index) => {
            amount.textContent = `$${priceList[priceKeys[index]]}`;
        });

        billingInfos.forEach(info => {
            info.textContent = billingText[duration];
        });
    }

    toggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            toggleButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            button.classList.add('active');
            
            // Update prices based on selected duration
            const duration = button.getAttribute('data-duration');
            updatePrices(duration);
        });
    });
});
