from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Trang chính
    path("", views.home, name="home"),

    # Sản phẩm & đơn hàng
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("product/<int:pk>/review/", views.submit_review, name="submit_review"),
    path("order/<int:pk>/", views.place_order, name="place_order"),
    path("order_success/", views.order_success, name="order_success"),

    # Các trang thông tin
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # Danh mục
    path("iphone/", views.iphone_products, name="iphone_products"),
    path("macbook/", views.macbook_products, name="macbook_products"),

    # Tài khoản
    path("signup/", views.signup_view, name="signup"),   # Đăng ký
    path("login/", auth_views.LoginView.as_view(
        template_name="login.html"
    ), name="login"),                                     # Đăng nhập
    path("logout/", auth_views.LogoutView.as_view(
        next_page="login"
    ), name="logout"),                                    # Đăng xuất

    # Giỏ hàng
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/remove/<int:cart_id>/", views.remove_from_cart, name="remove_from_cart"),

    # Thanh toán QR
    path("qr-checkout/", views.qr_checkout, name="qr_checkout"),
    path("qr-payment/<str:order_id>/", views.qr_payment, name="qr_payment"),
    path("check-payment-status/<str:order_id>/", views.check_payment_status, name="check_payment_status"),
    path("payment-success/<str:order_id>/", views.payment_success, name="payment_success"),
]
