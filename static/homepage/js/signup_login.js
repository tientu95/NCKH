const open_logins = document.querySelectorAll('.js-btn__open--login');
        const open_registers = document.querySelectorAll('.js-btn__open--register');
        const Closes = document.querySelectorAll('.js-btn__close');
        const modal_regis = document.querySelector('.js-modal__register');
        const modal_login = document.querySelector('.js-modal__login');
        const modalContainer = document.querySelector('.js-modal-container');
        const modal_container__login = document.querySelector('.js-modal-container__login')
        const modal_container__register = document.querySelector('.js-modal-container__register')
        // hàm mở modal lên
        function showRegister() {
            modal_regis.classList.add('open');
            modal_login.classList.remove('open');
        }
        function showLogin() {
            modal_login.classList.add('open');
            modal_regis.classList.remove('open');

        }
        // hàm đóng modal 
        function hideBuyTickets() {
            modal_regis.classList.remove('open');
            modal_login.classList.remove('open');
        }

        for(const open_register of open_registers){

            open_register.addEventListener('click', showRegister);
        }

        for(const open_login of open_logins){

            open_login.addEventListener('click', showLogin);
        }

        for(const Close of Closes){
            
            Close.addEventListener('click', hideBuyTickets);
        }
        modal.addEventListener('click', hideBuyTickets);
        modalContainer.addEventListener('click', function(even) {
            even.stopPropagation();
        })