function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

let content = $('#prRow');
let pagination = $('.pagination');
let cscs = "{% url 'store:product_detail' slug=product.slug %}"

$.ajax({
    type: "Get",
    url: "http://127.0.0.1:8000/api/v1/store/list",
    dataType: "json",
    success: function (resp) {
        for (let product of resp.results) {
            $(content).append(`<div class="col">
          <div class="card shadow-sm">
            <img class="img-fluid" alt="Responsive image" src="${ product.image }">
            <div class="card-body">
              <p class="card-text">
                <a class="text-dark text-decoration-none" href="${product.slug}">${ product.title }</a>
              </p>
              <div class="d-flex justify-content-between align-items-center">
                <small class="text-muted">lorem</small>
              </div>
            </div>
          </div>
        </div>`);


        }

        $(pagination).append(`<button id="previous" class="page btn btn-secondary btn-sm" onclick="page('${resp.previous}')">&laquo;</button>`)
        for (let i = 1; i <= resp.num_pages; i++) {
            if (i === 1) {
                $(pagination).append(`
                    <button class="active page btn btn-secondary btn-sm" onclick="('http://127.0.0.1:8000/api/v1/store/list/?page=${i}')" disabled>${i}</button>`)
            } else {
                $(pagination).append(`
                    <button class="page page btn btn-secondary btn-sm" onclick="page('http://127.0.0.1:8000/api/v1/store/list/?page=${i}')">${i}</button>`)
            }
        }
        $(pagination).append(`<button id="next" class="page btn btn-secondary btn-sm" onclick="page('${resp.next}')">&raquo;</button>`);

        $('#previous').prop('disabled', true);
    }
});

function page(url) {
    if (url != null) {
        $.ajax({
            type: "Get",
            url: `${url}`,
            dataType: "json",
            success: function (resp) {
                $(content).empty();
                for (let product of resp.results) {
                    $(content).append(`<div class="col">
          <div class="card shadow-sm">
            <img class="img-fluid" alt="Responsive image" src="${ product.image }">
            <div class="card-body">
              <p class="card-text">
                <a class="text-dark text-decoration-none" href="${ product.get_absolute_url }">${ product.title }</a>
              </p>
              <div class="d-flex justify-content-between align-items-center">
                <small class="text-muted">lorem</small>
              </div>
            </div>
          </div>
        </div>`);


                }

                $(pagination).empty();
                $(pagination).append(`<button class="page page btn btn-secondary btn-sm" id="previous" onclick="page('${resp.previous}')">&laquo;</button>`)
                for (let i = 1; i <= resp.num_pages; i++) {
                    $(pagination).append(`
                        <button class="page page btn btn-secondary btn-sm" onclick="page('http://127.0.0.1:8000/api/v1/store/list?page=${i}')">${i}</button>`)
                }
                $(pagination).append(`<button id="next" class="page page btn btn-secondary btn-sm" onclick="page('${resp.next}')">&raquo;</button>`);

                if (url === 'http://127.0.0.1:8000/api/v1/store/list') {
                    url = 'http://127.0.0.1:8000/api/v1/store/list/';
                }

                $('.page').each(function () {
                    if ($(this).attr('onclick') === `page('${url}')`) {
                        $(this).attr('class', 'active');
                        $(this).prop('disabled', true);
                    }
                });

                if (resp.next == null) {
                    $('#next').prop('disabled', true);
                } else if (resp.previous == null) {
                    $('#previous').prop('disabled', true);
                }
            }
        });
    }
}