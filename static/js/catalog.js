$(document).ready(function() { // проверяем загружен ли DOM

$('h2:first').addClass('active'); //добавляем класс .active к первому блоку 
$('.toggle_container:not(:first)').hide(); // оставляем открытым первый блок

$('h2.trigger').click(function() { 
	$(this).toggleClass('active').next().slideToggle('slow').siblings("div:visible").slideUp('slow'); // при клике раскрываем блок и закрываем другие видимые блоки
	$(this).siblings('h2').removeClass('active'); // удаляем класс .active у родственных блоков
	return false; // возвращаем false для запрета перехода по ссылке
});
});