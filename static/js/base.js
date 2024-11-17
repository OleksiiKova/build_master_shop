// Bootstrap Toast: Show toast notification on page load if present
document.addEventListener('DOMContentLoaded', function () {
    var toastEl = document.querySelector('.toast');
    if (toastEl) {
        var toast = new bootstrap.Toast(toastEl);
        toast.show();
    }
});

// Back-to-Top Button: Show/hide button based on scroll position and scroll to top on click
document.addEventListener('DOMContentLoaded', function () {
    const backToTopButton = document.getElementById('backToTop');

    if (backToTopButton) {
        backToTopButton.addEventListener('click', function (event) {
            event.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });

        window.addEventListener('scroll', function () {
            if (window.scrollY > 100) {
                backToTopButton.classList.add('show');
            } else {
                backToTopButton.classList.remove('show');
            }
        });
    }
});

// Dropdown Submenu: Toggle visibility for mobile and desktop devices
$(document).ready(function () {
    var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    $('.dropdown-submenu > a').on('click touchstart', function (e) {
        var submenu = $(this).next('.dropdown-menu');

        if (isMobile && !submenu.is(':visible')) {
            submenu.show();
            e.preventDefault();
        } else if (!isMobile && !submenu.is(':visible')) {
            submenu.show();
            e.preventDefault();
        } else {
            return true;
        }
    });
});

// MailChimp Form Fields: Define field names and types for integration
(function ($) {
    window.fnames = [];
    window.ftypes = [];
    fnames[0] = 'EMAIL';
    ftypes[0] = 'email';
    fnames[1] = 'FNAME';
    ftypes[1] = 'text';
    fnames[2] = 'LNAME';
    ftypes[2] = 'text';
    fnames[3] = 'ADDRESS';
    ftypes[3] = 'address';
    fnames[4] = 'PHONE';
    ftypes[4] = 'phone';
    fnames[5] = 'BIRTHDAY';
    ftypes[5] = 'birthday';
    fnames[6] = 'COMPANY';
    ftypes[6] = 'text';
}(jQuery));
var $mcj = jQuery.noConflict(true);