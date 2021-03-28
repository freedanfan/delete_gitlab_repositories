# 批量删除Github仓库脚本

**背景**：由于手动删除GitHub的流程较多，使用脚本能够实现批量删除GitHub的仓库



**操作步骤**：

 1. 创建 具有删除权限的 token

    ```
    settings->Developer settings->Personal access tokens->Generate new token
    选择delete_repo
    ```

 2. 创建一个文件，例如命名为`repos.txt`，编写需要删除的库：

    ```
    # 用户名/仓库名
    usrname/repositoryname
    ```

 3. 运行脚本

    ```
    python delete_gitlab_repositories.py
    ```



### 参考：

1. [批量删除GitHub仓库](https://www.jianshu.com/p/308b85e1fe69)