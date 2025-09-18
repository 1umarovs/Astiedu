// $(document).ready(function () {
//     // Проверка, является ли устройство мобильным
//     var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
//
//     if (isMobile) {
//         // Мобильное устройство
//         $(".my-dropdown-btn").click(function (event) {
//             var $dropdownMenu = $(this).next('.dropdown-menu');
//             if ($dropdownMenu.hasClass('show')) {
//                 $dropdownMenu.removeClass('show');
//             } else {
//                 $('.dropdown-menu').removeClass('show'); // Скрыть другие открытые меню
//                 $dropdownMenu.addClass('show');
//             }
//             event.stopPropagation(); // Остановить всплытие события
//         });
//
//         // Закрыть меню при клике вне его
//         $(document).click(function () {
//             $('.dropdown-menu').removeClass('show');
//         });
//
//         // Остановить закрытие при клике на меню
//         $('.dropdown-menu').click(function (event) {
//             event.stopPropagation();
//         });
//     } else {
//         // Десктопное устройство
//         $(".my-dropdown-btn").hover(function () {
//             $(this).next('.dropdown-menu').addClass('show');
//         });
//
//         $('.dropdown-menu').hover(function () {
//             $(this).addClass('show');
//         }, function () {
//             $(this).removeClass('show');
//         });
//
//         $(".my-dropdown-btn").mouseout(function () {
//             var self = this;
//             setTimeout(function() {
//                 if (!$('.dropdown-menu:hover').length) {
//                     $(self).next('.dropdown-menu').removeClass('show');
//                 }
//             }, 300);
//         });
//
//         $('.dropdown-menu').mouseout(function () {
//             var self = this;
//             setTimeout(function() {
//                 if (!$('.my-dropdown-btn:hover').length && !$('.dropdown-menu:hover').length) {
//                     $(self).removeClass('show');
//                 }
//             }, 300);
//         });
//     }
// });
