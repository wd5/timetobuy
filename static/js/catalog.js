$(document).ready(function() { // ��������� �������� �� DOM

$('h2:first').addClass('active'); //��������� ����� .active � ������� ����� 
$('.toggle_container:not(:first)').hide(); // ��������� �������� ������ ����

$('h2.trigger').click(function() { 
	$(this).toggleClass('active').next().slideToggle('slow').siblings("div:visible").slideUp('slow'); // ��� ����� ���������� ���� � ��������� ������ ������� �����
	$(this).siblings('h2').removeClass('active'); // ������� ����� .active � ����������� ������
	return false; // ���������� false ��� ������� �������� �� ������
});
});