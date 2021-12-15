    const openBtn = document.querySelector('.js-btn__open');
    const modal = document.querySelector('.js-modal');
    const CloseBtn = document.querySelector('.js-btn__close');
    const modalContainer = document.querySelector('.js-modal-container');
    // hàm mở modal lên
    function showBuyTickets() {
        modal.classList.add('open');
    }
    // hàm đóng modal 
    function hideBuyTickets() {
        modal.classList.remove('open');
    }
        openBtn.addEventListener('click', showBuyTickets);
        CloseBtn.addEventListener('click', hideBuyTickets);
        modal.addEventListener('click', hideBuyTickets);
        modalContainer.addEventListener('click', function(even) {
            even.stopPropagation();
        })