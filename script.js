document.addEventListener('DOMContentLoaded', function () {
    const IP_LOOKUP_URL = 'https://api64.ipify.org?format=json';
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
    let clientIpPromise = null;

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
        '+852': {
            pattern: /^[0-9]{8}$/,
            message: '請輸入8位數字',
            alert: '香港電話號碼必須是8位數字',
            placeholder: '請輸入8位數字'
        },
        '+86': {
            pattern: /^[0-9]{11}$/,
            message: '請輸入11位數字',
            alert: '內地電話號碼必須是11位數字',
            placeholder: '請輸入11位數字'
        }
    };

    function updatePhoneHint() {
        const rule = phoneRules[areaCodeSelect.value];
        if (!rule) {
            phoneHint.style.color = '#666';
            phoneHint.textContent = '請輸入有效電話號碼';
            phoneInput.placeholder = '請輸入電話號碼';
            return;
        }

        phoneHint.style.color = '#666';
        phoneHint.textContent = rule.message;
        phoneInput.placeholder = rule.placeholder;
    }

    function validatePhoneNumber(phone, areaCode) {
        const rule = phoneRules[areaCode];
        if (!rule) {
            return false;
        }

        return rule.pattern.test(phone.replace(/[-\\s]/g, ''));
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

    function loadClientIp() {
        if (!clientIpPromise) {
            clientIpPromise = fetch(IP_LOOKUP_URL, {
                method: 'GET',
                cache: 'no-store'
            })
                .then(function (response) {
                    if (!response.ok) {
                        throw new Error('IP lookup failed');
                    }

                    return response.json();
                })
                .then(function (data) {
                    return typeof data.ip === 'string' ? data.ip : '';
                })
                .catch(function (error) {
                    console.warn('IP lookup failed:', error);
                    return '';
                });
        }

        return clientIpPromise;
    }

    function getInquiryType() {
        const checked = contactForm.querySelector('input[name="zxsx"]:checked, input[name="zxsx1"]:checked');
        if (checked) {
            return checked.value;
        }

        return '';
    }

    function buildPayload(clientIp) {
        const payload = new URLSearchParams();

        payload.append('submitted_at', new Date().toISOString());
        payload.append('site', document.body.dataset.site || 'hk-main');
        payload.append('language', document.documentElement.lang || 'zh-HK');
        payload.append('page_title', document.title);
        payload.append('page_url', window.location.href);
        payload.append('name', document.getElementById('name').value.trim());
        payload.append('area_code', areaCodeSelect.value);
        payload.append('phone', phoneInput.value.trim().replace(/[-\\s]/g, ''));
        payload.append('wechat', (document.getElementById('wechat').value || '').trim());
        payload.append('inquiry_type', getInquiryType());
        payload.append('message', (document.getElementById('message').value || '').trim());
        payload.append('source', 'github-pages');
        payload.append('user_agent', navigator.userAgent);
        payload.append('client_ip', clientIp || '');

        return payload;
    }

    areaCodeSelect.addEventListener('change', updatePhoneHint);

    phoneInput.addEventListener('input', function () {
        const phone = phoneInput.value.trim();

        if (!phone) {
            updatePhoneHint();
            return;
        }

        if (validatePhoneNumber(phone, areaCodeSelect.value)) {
            phoneHint.style.color = '#4CAF50';
            phoneHint.textContent = '✓ 格式正確';
        } else {
            phoneHint.style.color = '#ff4444';
            phoneHint.textContent = phoneRules[areaCodeSelect.value]
                ? phoneRules[areaCodeSelect.value].message
                : '請輸入有效電話號碼';
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
            alert('請填寫您的稱呼');
            return;
        }

        if (!phone) {
            alert('請填寫聯絡電話');
            return;
        }

        if (!validatePhoneNumber(phone, areaCode)) {
            const rule = phoneRules[areaCode];
            alert(rule ? rule.alert : '請輸入有效電話號碼');
            phoneInput.focus();
            return;
        }

        if (!endpoint || endpoint.includes('PASTE_GOOGLE_APPS_SCRIPT_WEB_APP_URL_HERE')) {
            alert('Google 表格接口還沒配置，請先在 site-config.js 填入 Apps Script Web App URL。');
            return;
        }

        const submitBtn = contactForm.querySelector('.submit-btn');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = '提交中...';
        submitBtn.disabled = true;

        try {
            const clientIp = await loadClientIp();

            await fetch(endpoint, {
                method: 'POST',
                mode: 'no-cors',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                },
                body: buildPayload(clientIp).toString()
            });

            showSuccessModal();
            resetForm();

            if (typeof gtag !== 'undefined') {
                gtag('event', 'conversion', { 'send_to': 'AW-18003046397/yLGoCM6KjowcEP3fwohD' });
            }
        } catch (error) {
            console.error('Submission failed:', error);
            alert('提交過程中發生錯誤，請稍後再試');
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

    loadClientIp();
    updatePhoneHint();
});
