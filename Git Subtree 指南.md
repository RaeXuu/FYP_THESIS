**Git Subtree 同步指南**                                                

**前提：仓库C已初始化并有至少一次提交**                                 

  ---                                                                 

  **第一步：在原仓库（repo-a）拆分子目录**

  cd /path/to/repo-a

  # 把 markdown/ 文件夹拆成独立分支                                   

  `git subtree split --prefix=markdown -b markdown-only`

  # 推到 GitHub                                                       

  git push origin markdown-only

  ---             

  **第二步：在仓库C添加远程并引入内容**

  cd /path/to/repo-c

  # 添加远程（只需做一次）

  git remote add FYP_rasp https://github.com/RaeXuu/FYP_raspberry_pi.git
  git remote add FYP_PC https://github.com/RaeXuu/FYP.git

  # 引入内容到指定文件夹                                              

  git subtree add --prefix=notes-from-pi FYP_rasp markdown-only  --squash           
  git subtree add --prefix=notes-from-PC FYP_PC markdown-only  --squash

  ---

  **日常同步**

  **从 repo-a 拉取最新内容到仓库C：**

  git subtree pull --prefix=notes-from-pi FYP_rasp markdown-only  --squash               git subtree pull --prefix=notes-from-PC FYP_PC markdown-only  --squash                                        

  **把仓库C的修改推回 repo-a：**

  git subtree push --prefix=notes-from-pi FYP_rasp markdown-only      
  git subtree push --prefix=notes-from-PC FYP_PC markdown-only     
  ---                                                       
  