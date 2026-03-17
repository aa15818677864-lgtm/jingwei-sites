document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');
    const header = document.querySelector('.header');
    const fadeElements = document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right');
    const contactUsBtn = document.getElementById('contactUsBtn');
    const areaCodeSelect = document.getElementById('areaCode');
    const phoneInput = document.getElementById('phone');
    const phoneHint = document.getElementById('phoneHint');
    const contactForm = document.getElementById('contactForm');
    const successModal = document.getElementById('successModal');
    const modalCloseBtn = document.getElementById('modalCloseBtn');

    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function () {
            navMenu.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });

        document.querySelectorAll('.nav a').forEach(function (link) {
            link.addEventListener('click', function () {
                if (window.innerWidth <= 768) {
                    navMenu.classList.remove('active');
                    menuToggle.classList.remove('active');
                }
            });
        });

        window.addEventListener('resize', function () {
            if (window.innerWidth > 768) {
                navMenu.classList.remove('active');
                menuToggle.classList.remove('active');
            }
        });
    }

    if (header) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    if (fadeElements.length) {
        if ('IntersectionObserver' in window) {
            const appearOnScroll = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        const delay = Array.from(fadeElements).indexOf(entry.target) * 30;
                        setTimeout(function () {
                            entry.target.classList.add('visible');
                        }, delay);
                        appearOnScroll.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            });

            fadeElements.forEach(function (element) {
                appearOnScroll.observe(element);
            });
        } else {
            fadeElements.forEach(function (element) {
                element.classList.add('visible');
            });
        }
    }

    if (contactUsBtn) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 300) {
                contactUsBtn.classList.add('visible');
            } else {
                contactUsBtn.classList.remove('visible');
            }
        });

        contactUsBtn.addEventListener('click', function () {
            const contactSection = document.getElementById('contact');
            if (!contactSection || !header) {
                return;
            }

            const targetPosition = contactSection.getBoundingClientRect().top + window.pageYOffset - header.offsetHeight;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (event) {
            event.preventDefault();

            const targetId = anchor.getAttribute('href');
            if (!targetId || targetId === '#') {
                return;
            }

            const targetElement = document.querySelector(targetId);
            if (!targetElement || !header) {
                return;
            }

            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - header.offsetHeight;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        });
    });

    window.addEventListener('load', function () {
        document.body.classList.add('loaded');
    });

    if (!areaCodeSelect || !phoneInput || !phoneHint || !contactForm || !successModal || !modalCloseBtn) {
        return;
    }

    const phoneRules = {
        '+60': {
            pattern: /^[0-9]{9,11}$/,
            message_zh: '請輸入9-11位數字（如：123456789）',
            message_en: 'Please enter 9-11 digits (e.g., 123456789)',
            alert_zh: '馬來西亞電話號碼必須是9-11位數字',
            alert_en: 'Malaysian phone number must be 9-11 digits',
            placeholder_zh: '請輸入9-11位數字',
            placeholder_en: 'Enter 9-11 digits'
        },
        '+65': {
            pattern: /^[0-9]{8}$/,
            message_zh: '請輸入8位數字',
            message_en: 'Please enter 8 digits',
            alert_zh: '新加坡電話號碼必須是8位數字',
            alert_en: 'Singapore phone number must be 8 digits',
            placeholder_zh: '請輸入8位數字',
            placeholder_en: 'Enter 8 digits'
        },
        '+86': {
            pattern: /^[0-9]{11}$/,
            message_zh: '請輸入11位數字',
            message_en: 'Please enter 11 digits',
            alert_zh: '內地電話號碼必須是11位數字',
            alert_en: 'Mainland phone number must be 11 digits',
            placeholder_zh: '請輸入11位數字',
            placeholder_en: 'Enter 11 digits'
        }
    };

    function getCurrentLanguage() {
        return document.documentElement.lang.includes('zh') ? 'zh' : 'en';
    }

    function getText(zh, en) {
        return getCurrentLanguage() === 'zh' ? zh : en;
    }

    function updatePhoneHint() {
        const rule = phoneRules[areaCodeSelect.value];
        const lang = getCurrentLanguage();

        if (!rule) {
            phoneHint.style.color = '#666';
            phoneHint.textContent = getText('請輸入有效電話號碼', 'Please enter a valid phone number');
            phoneInput.placeholder = getText('請輸入電話號碼', 'Enter your phone number');
            return;
        }

        phoneHint.style.color = '#666';
        phoneHint.textContent = rule['message_' + lang];
        phoneInput.placeholder = rule['placeholder_' + lang];
    }

    function validatePhoneNumber(phone, areaCode) {
        const rule = phoneRules[areaCode];
        if (!rule) {
            return false;
        }

        return rule.pattern.test(phone.replace(/[-\s]/g, ''));
    }

    function showSuccessModal() {
        successModal.style.display = 'flex';
        setTimeout(function () {
            if (successModal.style.display === 'flex') {
                successModal.style.display = 'none';
            }
        }, 3000);
    }

    function resetForm() {
        const currentAreaCode = areaCodeSelect.value;
        contactForm.reset();
        areaCodeSelect.value = currentAreaCode;
        updatePhoneHint();
    }

    function getFormEndpoint() {
        if (!window.SITE_CONFIG || typeof window.SITE_CONFIG.googleSheetsEndpoint !== 'string') {
            return '';
        }

        return window.SITE_CONFIG.googleSheetsEndpoint.trim();
    }

    function buildPayload() {
        const selectedInquiry = contactForm.querySelector('input[name="zxsx"]:checked');
        const payload = new URLSearchParams();

        payload.append('submitted_at', new Date().toISOString());
        payload.append('site', document.body.dataset.site || '');
        payload.append('language', getCurrentLanguage());
        payload.append('page_title', document.title);
        payload.append('page_url', window.location.href);
        payload.append('name', document.getElementById('name').value.trim());
        payload.append('area_code', areaCodeSelect.value);
        payload.append('phone', phoneInput.value.trim().replace(/[-\s]/g, ''));
        payload.append('wechat', (document.getElementById('wechat').value || '').trim());
        payload.append('inquiry_type', selectedInquiry ? selectedInquiry.value : '');
        payload.append('message', (document.getElementById('message').value || '').trim());
        payload.append('source', 'github-pages');
        payload.append('user_agent', navigator.userAgent);

        return payload;
    }

    areaCodeSelect.addEventListener('change', updatePhoneHint);

    phoneInput.addEventListener('input', function () {
        const phone = phoneInput.value.trim();
        const lang = getCurrentLanguage();

        if (!phone) {
            updatePhoneHint();
            return;
        }

        if (validatePhoneNumber(phone, areaCodeSelect.value)) {
            phoneHint.style.color = '#4CAF50';
            phoneHint.textContent = lang === 'zh' ? '✓ 格式正確' : '✓ Format correct';
        } else {
            phoneHint.style.color = '#ff4444';
            phoneHint.textContent = phoneRules[areaCodeSelect.value]
                ? phoneRules[areaCodeSelect.value]['message_' + lang]
                : getText('請輸入有效電話號碼', 'Please enter a valid phone number');
        }
    });

    contactForm.addEventListener('submit', async function (event) {
        event.preventDefault();
        document.getElementById('page_url').value = window.location.href;

        const name = document.getElementById('name').value.trim();
        const phone = phoneInput.value.trim();
        const areaCode = areaCodeSelect.value;
        const endpoint = getFormEndpoint();

        if (!name) {
            alert(getText('請填寫您的稱呼', 'Please enter your name'));
            return;
        }

        if (!phone) {
            alert(getText('請填寫聯絡電話', 'Please enter contact number'));
            return;
        }

        if (!validatePhoneNumber(phone, areaCode)) {
            const rule = phoneRules[areaCode];
            alert(rule ? rule['alert_' + getCurrentLanguage()] : getText('請輸入有效的電話號碼', 'Please enter a valid phone number'));
            phoneInput.focus();
            return;
        }

        if (!endpoint || endpoint.includes('PASTE_GOOGLE_APPS_SCRIPT_WEB_APP_URL_HERE')) {
            alert(getText(
                'Google 表格接口還沒配置，請先在 site-config.js 填入 Apps Script Web App URL。',
                'Google Sheets is not configured yet. Please paste the Apps Script Web App URL into site-config.js first.'
            ));
            return;
        }

        const submitBtn = contactForm.querySelector('.submit-btn');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = getText('提交中...', 'Submitting...');
        submitBtn.disabled = true;

        try {
            await fetch(endpoint, {
                method: 'POST',
                mode: 'no-cors',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                },
                body: buildPayload().toString()
            });

            showSuccessModal();
            resetForm();

            if (typeof gtag !== 'undefined') {
                gtag('event', 'conversion', { 'send_to': 'AW-17710767718/PU98CKzsxLsbEOa8k_1B' });
            }
        } catch (error) {
            console.error('Submission failed:', error);
            alert(getText('提交失敗，請稍後再試。', 'Submission failed. Please try again later.'));
        } finally {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });

    modalCloseBtn.addEventListener('click', function () {
        successModal.style.display = 'none';
    });

    successModal.addEventListener('click', function (event) {
        if (event.target === successModal) {
            successModal.style.display = 'none';
        }
    });

    updatePhoneHint();
});
