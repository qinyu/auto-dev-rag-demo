Feature: 上传 PDF 文档
  作为用户，
  我想要能够上传 PDF 文档，
  以便于我可以在博客网站上分享和展示我的文档。

  Scenario: 上传有效的 PDF 文档
    Given 用户选择上传一个有效的 PDF 文档，
    When 用户点击上传按钮时，
    Then 系统应该成功接收并保存该文档。

  Scenario: 处理上传的异常文件格式
    Given 用户选择上传一个非 PDF 格式的文件，
    When 用户点击上传按钮时，
    Then 系统应该提示用户只能上传 PDF 格式的文件。

  Scenario: 处理上传的空文件
    Given 用户选择上传一个空文件，
    When 用户点击上传按钮时，
    Then 系统应该提示用户不能上传空文件。