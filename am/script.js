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

    function getCurrentLanguage() {
        return document.documentElement.lang.includes('zh') ? 'zh' : 'en';
    }

    function getText(zh, en) {
        return getCurrentLanguage() === 'zh' ? zh : en;
    }

    document.querySelectorAll('section:not(.hero) img').forEach(function (image) {
        if (!image.hasAttribute('loading')) {
            image.setAttribute('loading', 'lazy');
        }

        image.setAttribute('decoding', 'async');
        image.setAttribute('fetchpriority', 'low');
    });

    const mobileCollapsibles = [
        {
            key: 'issues',
            container: document.querySelector('[data-mobile-toggle="issues"]')
        },
        {
            key: 'team',
            container: document.querySelector('[data-mobile-toggle="team"]')
        }
    ];

    mobileCollapsibles.forEach(function (section) {
        if (!section.container || !section.container.parentNode) {
            return;
        }

        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'mobile-collapse-toggle';
        button.dataset.toggleTarget = section.key;
        section.container.insertAdjacentElement('afterend', button);
        section.button = button;
    });

    function getCollapseButtonLabel(key, expanded) {
        if (key === 'issues') {
            return expanded
                ? getText('\u6536\u8d77\u6cd5\u5f8b\u95ee\u9898', 'Show fewer issues')
                : getText('\u5c55\u5f00\u5269\u4f59\u5185\u5bb9', 'Show the rest');
        }

        return expanded
            ? getText('\u6536\u8d77\u5f8b\u5e08\u56e2\u961f', 'Show fewer lawyers')
            : getText('\u5c55\u5f00\u5269\u4f59\u5f8b\u5e08', 'Show more lawyers');
    }

    function setMobileCollapsibleState(section, expanded) {
        if (!section.container || !section.button) {
            return;
        }

        section.container.classList.toggle('is-expanded', expanded);
        section.container.classList.toggle('is-collapsed', !expanded);
        section.button.textContent = getCollapseButtonLabel(section.key, expanded);
        section.button.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    }

    function syncMobileCollapsible(section) {
        if (!section.container || !section.button) {
            return;
        }

        if (window.innerWidth > 768) {
            section.button.hidden = true;
            setMobileCollapsibleState(section, true);
            return;
        }

        const expanded = section.container.dataset.mobileExpanded === 'true';
        section.button.hidden = false;
        setMobileCollapsibleState(section, expanded);
    }

    mobileCollapsibles.forEach(function (section) {
        if (!section.container || !section.button) {
            return;
        }

        section.container.dataset.mobileExpanded = 'false';

        section.button.addEventListener('click', function () {
            const nextExpanded = section.container.dataset.mobileExpanded !== 'true';
            section.container.dataset.mobileExpanded = nextExpanded ? 'true' : 'false';
            setMobileCollapsibleState(section, nextExpanded);
        });

        syncMobileCollapsible(section);
    });

    if (mobileCollapsibles.some(function (section) { return section.container && section.button; })) {
        window.addEventListener('resize', function () {
            mobileCollapsibles.forEach(syncMobileCollapsible);
        });
    }

    if (!areaCodeSelect || !phoneInput || !phoneHint || !contactForm || !successModal || !modalCloseBtn) {
        return;
    }

    const submitBtn = contactForm.querySelector('.submit-btn');
    let submitFeedback = null;

    if (submitBtn) {
        submitFeedback = document.createElement('div');
        submitFeedback.className = 'submit-feedback';
        submitFeedback.setAttribute('aria-live', 'polite');
        submitFeedback.hidden = true;
        submitBtn.insertAdjacentElement('afterend', submitFeedback);
    }

    const phoneRules = {
        '+60': {
            pattern: /^[0-9]{9,11}$/,
            message_zh: '\u8acb\u8f38\u51659-11\u4f4d\u6578\u5b57\uff08\u5982\uff1a123456789\uff09',
            message_en: 'Please enter 9-11 digits (e.g., 123456789)',
            alert_zh: '\u99ac\u4f86\u897f\u4e9e\u96fb\u8a71\u865f\u78bc\u5fc5\u9808\u662f9-11\u4f4d\u6578\u5b57',
            alert_en: 'Malaysian phone number must be 9-11 digits',
            placeholder_zh: '\u8acb\u8f38\u51659-11\u4f4d\u6578\u5b57',
            placeholder_en: 'Enter 9-11 digits'
        },
        '+65': {
            pattern: /^[0-9]{8}$/,
            message_zh: '\u8acb\u8f38\u51658\u4f4d\u6578\u5b57',
            message_en: 'Please enter 8 digits',
            alert_zh: '\u65b0\u52a0\u5761\u96fb\u8a71\u865f\u78bc\u5fc5\u9808\u662f8\u4f4d\u6578\u5b57',
            alert_en: 'Singapore phone number must be 8 digits',
            placeholder_zh: '\u8acb\u8f38\u51658\u4f4d\u6578\u5b57',
            placeholder_en: 'Enter 8 digits'
        },
        '+86': {
            pattern: /^[0-9]{11}$/,
            message_zh: '\u8acb\u8f38\u516511\u4f4d\u6578\u5b57',
            message_en: 'Please enter 11 digits',
            alert_zh: '\u5167\u5730\u96fb\u8a71\u865f\u78bc\u5fc5\u9808\u662f11\u4f4d\u6578\u5b57',
            alert_en: 'Mainland phone number must be 11 digits',
            placeholder_zh: '\u8acb\u8f38\u516511\u4f4d\u6578\u5b57',
            placeholder_en: 'Enter 11 digits'
        }
    };

    function updatePhoneHint() {
        const rule = phoneRules[areaCodeSelect.value];
        const lang = getCurrentLanguage();

        if (!rule) {
            phoneHint.style.color = '#666';
            phoneHint.textContent = getText('\u8acb\u8f38\u5165\u6709\u6548\u96fb\u8a71\u865f\u78bc', 'Please enter a valid phone number');
            phoneInput.placeholder = getText('\u8acb\u8f38\u5165\u96fb\u8a71\u865f\u78bc', 'Enter your phone number');
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

    function wait(ms) {
        return new Promise(function (resolve) {
            window.setTimeout(resolve, ms);
        });
    }

    function setSubmitFeedback(type, message) {
        if (!submitFeedback) {
            return;
        }

        submitFeedback.className = 'submit-feedback';

        if (type) {
            submitFeedback.classList.add('is-' + type);
        }

        submitFeedback.textContent = message || '';
        submitFeedback.hidden = !message;
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

    function buildPayload(clientIp) {
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
        payload.append('client_ip', clientIp || '');

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
            phoneHint.textContent = lang === 'zh' ? '\u2713 \u683c\u5f0f\u6b63\u78ba' : '\u2713 Format correct';
        } else {
            phoneHint.style.color = '#ff4444';
            phoneHint.textContent = phoneRules[areaCodeSelect.value]
                ? phoneRules[areaCodeSelect.value]['message_' + lang]
                : getText('\u8acb\u8f38\u5165\u6709\u6548\u96fb\u8a71\u865f\u78bc', 'Please enter a valid phone number');
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
            alert(getText('\u8acb\u586b\u5beb\u60a8\u7684\u7a31\u547c', 'Please enter your name'));
            return;
        }

        if (!phone) {
            alert(getText('\u8acb\u586b\u5beb\u806f\u7d61\u96fb\u8a71', 'Please enter contact number'));
            return;
        }

        if (!validatePhoneNumber(phone, areaCode)) {
            const rule = phoneRules[areaCode];
            alert(rule ? rule['alert_' + getCurrentLanguage()] : getText('\u8acb\u8f38\u5165\u6709\u6548\u7684\u96fb\u8a71\u865f\u78bc', 'Please enter a valid phone number'));
            phoneInput.focus();
            return;
        }

        if (!endpoint || endpoint.includes('PASTE_GOOGLE_APPS_SCRIPT_WEB_APP_URL_HERE')) {
            alert(getText(
                'Google \u8868\u683c\u63a5\u53e3\u9084\u6c92\u914d\u7f6e\uff0c\u8acb\u5148\u5728 site-config.js \u586b\u5165 Apps Script Web App URL\u3002',
                'Google Sheets is not configured yet. Please paste the Apps Script Web App URL into site-config.js first.'
            ));
            return;
        }

        if (!submitBtn) {
            return;
        }

        const originalText = submitBtn.textContent;
        submitBtn.textContent = getText('\u6b63\u5728\u63d0\u4ea4\uff0c\u8bf7\u7a0d\u5019...', 'Submitting, please wait...');
        submitBtn.disabled = true;
        submitBtn.classList.add('is-loading');
        setSubmitFeedback(
            'loading',
            getText('\u6b63\u5728\u5b89\u5168\u63d0\u4ea4\u60a8\u7684\u8d44\u6599\uff0c\u8bf7\u7a0d\u5019 1-2 \u79d2\u2026', 'Securely sending your details, please wait 1-2 seconds...')
        );

        try {
            const clientIp = await loadClientIp();

            await Promise.all([
                fetch(endpoint, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                    },
                    body: buildPayload(clientIp).toString()
                }),
                wait(900)
            ]);

            setSubmitFeedback(
                'success',
                getText('\u63d0\u4ea4\u6210\u529f\uff0c\u6b63\u5728\u4e3a\u60a8\u663e\u793a\u786e\u8ba4\u4fe1\u606f\u2026', 'Sent successfully. Preparing your confirmation...')
            );
            showSuccessModal();
            resetForm();

            if (typeof gtag !== 'undefined') {
                gtag('event', 'conversion', { 'send_to': 'AW-18003046397/yLGoCM6KjowcEP3fwohD' });
            }
        } catch (error) {
            console.error('Submission failed:', error);
            setSubmitFeedback(
                'error',
                getText('\u63d0\u4ea4\u5931\u8d25\uff0c\u8bf7\u7a0d\u5019\u91cd\u8bd5\u3002', 'Submission failed. Please try again in a moment.')
            );
            alert(getText('\u63d0\u4ea4\u5931\u6557\uff0c\u8acb\u7a0d\u5f8c\u518d\u8a66\u3002', 'Submission failed. Please try again later.'));
        } finally {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
            submitBtn.classList.remove('is-loading');
            window.setTimeout(function () {
                setSubmitFeedback('', '');
            }, 1800);
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
