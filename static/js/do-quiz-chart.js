
$(function () {

    var $doQuizChart = $("#do-quiz-chart");
    $.ajax({
    url: $doQuizChart.data("url"),
    success: function (data) {

        var ctx = $doQuizChart[0].getContext("2d");

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
            label: 'Quiz',
            backgroundColor: 'blue',
            data: data.data
            }]          
        },
        options: {
            responsive: true,
            legend: {
            position: 'top',
            },
            title: {
            display: true,
            text: 'Total of doing quiz Bar Chart'
            }
        }
        });

    }
    });

});

