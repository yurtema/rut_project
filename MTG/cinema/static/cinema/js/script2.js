
// Переменная для отслеживания текущего индекса события
let currentIndex = 0;

// Функция для загрузки событий
function loadEvents() {
    // Получаем все события
    const allEvents = document.querySelectorAll('.event');
    
    // Определяем индекс начала загрузки
    const startIndex = currentIndex;
    // Определяем индекс конца загрузки (максимум 4 события)
    const endIndex = Math.min(currentIndex + 4, allEvents.length);
    
    // Перебираем события, которые нужно показать
    for (let i = startIndex; i < endIndex; i++) {
        allEvents[i].style.display = 'block';
    }
    
    // Обновляем текущий индекс
    currentIndex = endIndex;
    
    // Если достигнут конец списка событий, скрываем кнопку
    if (currentIndex >= allEvents.length) {
        document.getElementById('loadMoreBtn').style.display = 'none';
    }
}

// Обработчик события нажатия на кнопку "Загрузить еще"
document.getElementById('loadMoreBtn').addEventListener('click', loadEvents);

// Запускаем загрузку событий при загрузке страницы
window.onload = loadEvents;
