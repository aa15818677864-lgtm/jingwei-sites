# 澳门、新加坡、美国 150 篇基础文章机制

更新时间：2026-07-24

## 目标

- 澳门、新加坡、美国各 50 个独立基础问题，共 150 个 story。
- 繁体、简体、英文是同一个 story 的三个页面，不重复计数。
- 50 是每个专题的完整基础知识框架，不是一次性批量上线指标。
- 旧单语文章先标记 `upgrade-required`，补齐研究、三语、唯一站内广告、SEO 和三轮审稿后才计入完成数。

## 选题结构

每个地区都覆盖以下层次，但标题和结论必须按当地制度重新研究，不能把“香港”替换成地区名：

1. 第一次处理时从哪里开始。
2. 死亡、亲属、遗嘱和身份文件。
3. 房产登记、共有、按揭、出租和出售。
4. 银行存款、福利款项和资金汇出。
5. 公司股权、分红和公司资料。
6. 授权、签字、文件跨境使用和原件交接。
7. 继承人失联、拒签、遗嘱争议和占用房产。
8. 未成年人、再婚家庭、放弃继承和二次继承。
9. 费用、债务、时间和转名后的管理。
10. 澳门、新加坡、美国各自特有的文件与程序问题。

完整 150 个题目由 `tools/regional_foundation_ops.py` 生成到本地台账 `content-system/regional-foundation-150.json`。

## 研究闸门

每篇至少有两类可核对的内部资料：

- 当地官方或司法机关的当前公开资料，确认当地文件、申请人、签发机关和程序作用。
- 内地接收机关、附加证明书或具体资产办理路径的当前资料，确认文件来到内地后解决什么问题。

研究记录保留标题、链接、查阅日期和支持的具体结论。正文向普通读者解释结论，不堆正式法规全名、政府链接或技术术语。

## 三轮实质审稿

文章进入 `ready` 或 `published` 前，必须有且只有三条完整审稿记录。每一轮都必须记录真实发现的问题、实际修改和验证证据；“没有问题”不能当作一次审稿。

1. **法律与地区事实**：核对人物、资产、文件用途、签发机关、条件性结论和地区差异。
2. **人类可读性**：分别用第一次处理继承、只想确认文件、家属不配合、年长手机读者、准备咨询的五种视角阅读，删除机器腔和重复模板。
3. **三语、站内广告、SEO 与移动端**：逐项核对事实一致性、英文自然改写、唯一 `.article-native-ad`、正确的法律助手链接、canonical、hreflang、Article JSON-LD、sitemap、内链和窄屏排版；不得残留旧三图组件。

## 状态流转

`planned -> researching -> drafting -> reviewing -> visuals -> ready -> published`

- `planned` 不能直接跳到 `published`。
- 任一研究或审稿证据缺失，允许停留，不为了数量上线。
- 推送和线上 URL 验证成功前不得登记 `published`。
- 已发布文章只在事实或用户体验确有改善时更新，不伪造发布日期。

## 操作命令

```powershell
python tools/regional_foundation_ops.py bootstrap
python tools/regional_foundation_ops.py audit
python tools/regional_foundation_ops.py summary
```

发布前仍需运行全站质量检查：

```powershell
python -m unittest discover -s tools -p "test_*.py" -v
python tools/article_ops.py audit
python tools/geo_hardening.py audit
python tools/article_inline_ad.py audit
git diff --check
```
