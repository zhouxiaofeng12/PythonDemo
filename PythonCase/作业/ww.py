import re
strA='com.koudai.weishop/com.koudai.weishop.order.page.list.OrderListActivity/android.view.ViewRootImpl @ e3b479c(visibility=8)'

strB= 'com.koudai.weishop/com.koudai.weishop.statistics.ui.activity.StatisticsMainActivity/android.view.ViewRootImpl @ 8b51480(visibility=8)'

print re.findall(r'.*page.list.(.*)/android.*',strA)
print re.findall(r'.*ui.activity.(.*)/android.*',strB)