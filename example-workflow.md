# Git 日常工作流程

## 1. 开始工作前 - 拉取最新代码
```bash
git pull origin master
```

## 2. 创建功能分支
```bash
git checkout -b feature-new-function
```

## 3. 开发和提交
```bash
# 修改文件...

# 查看更改
git status
git diff

# 添加并提交
git add .
git commit -m "描述你的更改"
```

## 4. 推送到远程
```bash
git push -u origin feature-new-function
```

## 5. 在 GitHub 上创建 Pull Request
- 访问仓库页面
- 点击 "Compare & pull request"
- 填写描述并创建

## 6. 合并后删除本地分支
```bash
git checkout master
git pull
git branch -d feature-new-function
```
