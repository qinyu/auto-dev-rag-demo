Feature: 可以上传演示视频
  作为一个InnoRev用户
  我想上传我的演示视频
  以便于我可以分享我的研究成果

  Scenario: 用户可以上传演示视频
    Given 用户已经登录InnoRev账户
    When 用户点击上传视频按钮
    Then 用户可以上传演示视频

  Scenario: 用户可以编辑上传的视频
    Given 用户已经上传了视频
    When 用户点击编辑视频按钮
    Then 用户可以编辑上传的视频,包括添加音乐、添加图片等

  Scenario: 用户可以删除上传的视频
    Given 用户已经上传了视频
    When 用户点击删除视频按钮
    Then 用户可以删除上传的视频