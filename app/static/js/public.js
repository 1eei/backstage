$(function () {
    /*登录验证*/

    // $('#submit').click(function (e) {
    //     let usernameLength = $('#name').val().length;
    //     let userpassLength = $('#password').val().length;
    //
    //     if (usernameLength === 0 || userpassLength === 0) {
    //         alert('账号密码不能为空');
    //         $('#name').val('')
    //         $('#password').val('')
    //         return false;
    //     }
    // });

    /*菜单栏按钮*/
    $('.X').click(function () {
        $(this).toggleClass('X-active');
        $('.index-control').toggleClass('toggle-control');
    });

    /*菜单栏按钮下拉*/
    $('.list-item1').bind('click', function (index) {
        $(this).next().toggleClass('toggle-item')
    });
    $('.list-item2 span').hover(function () {
        $(this).addClass('list-item1-active')
    }, function () {
        $(this).removeClass('list-item1-active')
    });

    $('.list-item1').bind('click', function (e) {
        $(this).children('p').toggleClass('tog-active')
    });


    /*翻页按钮选中状态*/
    $('.pub-pageTurning li').bind('click', function () {
        $(this).addClass('pub-pageActive');
        $(this).siblings('li').removeClass('pub-pageActive');
    });

    //条形图
    var ctx = document.getElementById('myChart');
    //气泡图
    var bubble = document.getElementById('myBubbleChart');
    //线图
    var line = document.getElementById('myLineChart');
    //饼状图
    var area = document.getElementById('myAreaChart');


    //条形图
    var BarData;
    var BarResult;
    $.ajax({
        url: "/post_bar_data",
        type: 'get',
        dataType: "json",
        cache: false,
        async: false,
        success: function (BarData) {
            Bar_Data = BarData[0].data
            Bar_Day = BarData[0].time
            BarResult = [Bar_Data, Bar_Day];
        }
    });

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: BarResult[1],
            datasets: [{
                label: '',
                data: BarResult[0],
                backgroundColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(244, 177, 77, 1)'
                ],
                borderColor: [
                    '#fff',
                    '#fff',
                    '#fff',
                    '#fff',
                    '#fff',
                    '#fff',
                    '#fff'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
            },
            legend: {
                display: false
            },
        }
    });


    //气泡图
    var BubbleData;
    var BubbleResult;
    $.ajax({
        url: "/post_bubble_data",
        type: 'get',
        dataType: "json",
        cache: false,
        async: false,
        success: function (BubbleData) {
            Bubble_Data = BubbleData[0].data
            BubbleResult = Bubble_Data;
        }
    });

    var myBubbleChart = new Chart(bubble, {
        type: 'bubble',
        data: {
            datasets: [{
                data: BubbleResult,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.4)',
                    'rgba(54, 162, 235, 0.4)',
                    'rgba(255, 206, 86, 0.4)',
                    'rgba(75, 192, 192, 0.4)',
                    'rgba(153, 102, 255, 0.4)',
                    'rgba(255, 159, 64, 0.4)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1

            }]
        },
        options: {
            legend: {
                display: false
            },
        }
    });


    //线状图
    var LineData;
    var LineResult;
    $.ajax({
        url: "/post_line_data",
        type: 'get',
        dataType: "json",
        cache: false,
        async: false,
        success: function (LineData) {
            Line_Data0 = LineData[0].data[0]
            Line_Data1 = LineData[0].data[1]
            Line_Data2 = LineData[0].data[2]
            Line_Data3 = LineData[0].data[3]
            Line_Day = LineData[0].time
            LineResult = [Line_Data0, Line_Data1, Line_Data2, Line_Data3, Line_Day];
        }
    });

    var myLineChart = new Chart(line, {
        type: 'line', // line 表示是 曲线图，当然也可以设置其他的图表类型 如柱形图 : bar  或者其他
        data: {
            labels: LineResult[4], //按时间段 可以按星期，按月，按年
            datasets: [{
                fill: false, //是否要显示数据部分阴影面积块
                borderColor: "rgba(200,187,205,1)", //数据曲线颜色
                pointBackgroundColor: "#fff", //数据点的颜色
                data: LineResult[0], //填充的数据
            },
                {
                    fill: false, //是否要显示数据部分阴影面积块
                    borderColor: "rgba(75,192,192,1)", //数据曲线颜色
                    pointBackgroundColor: "#fff", //数据点的颜色
                    data: LineResult[1], //填充的数据
                }, {
                    fill: false, //是否要显示数据部分阴影面积块
                    borderColor: "rgba(75,23,192,1)", //数据曲线颜色
                    pointBackgroundColor: "#fff", //数据点的颜色
                    data: LineResult[2], //填充的数据
                }, {
                    fill: false, //是否要显示数据部分阴影面积块
                    borderColor: "rgba(75,192,12,1)", //数据曲线颜色
                    pointBackgroundColor: "#fff", //数据点的颜色
                    data: LineResult[3], //填充的数据
                }
            ]
        },
        options: {
            legend: {
                display: false
            },
        }
    });


    //饼状图
    var AreaData;
    var AreaResult;
    $.ajax({
        url: "/post_area_data",
        type: 'get',
        dataType: "json",
        cache: false,
        async: false,
        success: function (AreaData) {
            AreaData = AreaData[0].data
            AreaResult = AreaData;
        }
    });

    var myAreaChart = new Chart(area, {
        data: {

            datasets: [{
                data: AreaResult,
                backgroundColor: [
                    'rgba(228, 66, 53, 1.00)',
                    'rgba(239, 188, 18, 1.00)',
                    'rgba(41, 197, 102, 1.00)',
                ]
            }],

            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: [
                '故障',
                '离线',
                '在线'
            ]

        },

        type: 'polarArea',
        options: {
            legend: {
                display: false
            },
        }
    });
})
