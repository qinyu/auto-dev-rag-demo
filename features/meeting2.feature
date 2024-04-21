Feature: 预订会议室
  作为一个小秘书，
  我想预订一个会议室，
  以便于我能够安排公司的会议。

  Scenario: 预订会议室
    Given 我已经登录到 InnoRev 网站，
    When 我点击“预订会议室”按钮时，
    Then 我被带到一个预订页面。

  Scenario: 选择会议室
    Given 我已经进入预订页面，
    When 我选择一个会议室时，
    Then 我可以看到该会议室的详细信息，包括容量、设备等。# Created by qinyu at 2024/4/21
