# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Zone: 可用区
        :type Zone: str
        :param NodeNum: 节点数量
        :type NodeNum: int
        :param EsVersion: 实例版本,当前只支持5.6.4
        :type EsVersion: str
        :param ChargeType: 计费类型: 
* PREPAID：预付费，即包年包月 
* POSTPAID_BY_HOUR：按小时后付费，默认值
        :type ChargeType: str
        :param ChargePeriod: 包年包月购买时长，单位：月
        :type ChargePeriod: int
        :param RenewFlag: 自动续费标识，取值范围： 
* NOTIFY_AND_AUTO_RENEW：通知过期且自动续费，默认值 
* NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费 
* DISABLE_NOTIFY_AND_MANUAL_RENEW： 不通知过期不自动续费
        :type RenewFlag: str
        :param NodeType: 节点规格 
* ES.S1.SMALL2: 1核2G
* ES.S1.MEDIUM4: 2核4G
* ES.S1.MEDIUM8: 2核8G
* ES.S1.LARGE16: 4核16G
* ES.S1.2XLARGE32: 8核32G
* ES.S1.3XLARGE32: 12核32G
* ES.S1.6XLARGE32: 24核32G
        :type NodeType: str
        :param DiskType: 节点存储类型,取值范围:  
* LOCAL_BASIC: 本地硬盘  
* LOCAL_SSD: 本地SSD硬盘，默认值  
* CLOUD_BASIC: 普通云硬盘  
* CLOUD_PREMIUM: 高硬能云硬盘  
* CLOUD_SSD: SSD云硬盘
        :type DiskType: str
        :param DiskSize: 节点存储容量，单位GB
        :type DiskSize: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Password: 访问密码，密码需8到16位，至少包括两项（[a-z,A-Z],[0-9]和[()`~!@#$%^&*-+=_|{}:;' <>,.?/]的特殊符号
        :type Password: str
        """
        self.InstanceName = None
        self.Zone = None
        self.NodeNum = None
        self.EsVersion = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.DiskType = None
        self.DiskSize = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.Zone = params.get("Zone")
        self.NodeNum = params.get("NodeNum")
        self.EsVersion = params.get("EsVersion")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 要销毁的实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 集群实例所属可用区，不传则默认所有可用区
        :type Zone: str
        :param InstanceIds: 一个或多个集群实例ID
        :type InstanceIds: list of str
        :param InstanceNames: 一个或多个集群实例名称
        :type InstanceNames: list of str
        :param Offset: 分页起始值, 默认值0
        :type Offset: int
        :param Limit: 分页大小，默认值20
        :type Limit: int
        :param OrderByKey: 排序字段：1，实例ID；2，实例名称；3，可用区；4，创建时间，若orderKey未传递则按创建时间降序排序
        :type OrderByKey: int
        :param OrderByType: 排序方式：0，升序；1，降序；若传递了orderByKey未传递orderByType, 则默认升序
        :type OrderByType: int
        """
        self.Zone = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderByType = params.get("OrderByType")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的实例个数
        :type TotalCount: int
        :param InstanceList: 实例详细信息列表
        :type InstanceList: list of InstanceInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param AppId: 用户ID
        :type AppId: int
        :param Uin: 用户UIN
        :type Uin: str
        :param VpcUid: 实例所属VPC的UID
        :type VpcUid: str
        :param SubnetUid: 实例所属子网的UID
        :type SubnetUid: str
        :param Status: 实例状态，0:处理中,1:正常,-1停止,-2:销毁中,-3:已销毁
        :type Status: int
        :param ChargeType: 实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
        :type ChargeType: str
        :param ChargePeriod: 包年包月购买时长,单位:月
        :type ChargePeriod: int
        :param RenewFlag: 自动续费标识。取值范围：  NOTIFY_AND_AUTO_RENEW：通知过期且自动续费  NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费  DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费  默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        :param NodeType: 节点规格:  ES.S1.SMALL2 : 1核2G  ES.S1.MEDIUM4 : 2核4G  ES.S1.MEDIUM8 : 2核8G  ES.S1.LARGE16 : 4核16G  ES.S1.2XLARGE32 : 8核32G  ES.S1.3XLARGE32 : 12核32G  ES.S1.6XLARGE32 : 24核32G
        :type NodeType: str
        :param NodeNum: 节点个数
        :type NodeNum: int
        :param CpuNum: 节点CPU核数
        :type CpuNum: int
        :param MemSize: 节点内存大小，单位GB
        :type MemSize: int
        :param DiskType: 节点磁盘类型
        :type DiskType: str
        :param DiskSize: 节点磁盘大小，单位GB
        :type DiskSize: int
        :param EsDomain: ES域名
        :type EsDomain: str
        :param EsVip: ES VIP
        :type EsVip: str
        :param EsPort: ES端口
        :type EsPort: int
        :param KibanaUrl: Kibana访问url
        :type KibanaUrl: str
        :param EsVersion: ES版本号
        :type EsVersion: str
        :param EsConfig: ES配置项
        :type EsConfig: str
        :param EsAcl: ES访问控制配置
        :type EsAcl: str
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param UpdateTime: 实例最后修改操作时间
        :type UpdateTime: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.AppId = None
        self.Uin = None
        self.VpcUid = None
        self.SubnetUid = None
        self.Status = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.NodeNum = None
        self.CpuNum = None
        self.MemSize = None
        self.DiskType = None
        self.DiskSize = None
        self.EsDomain = None
        self.EsVip = None
        self.EsPort = None
        self.KibanaUrl = None
        self.EsVersion = None
        self.EsConfig = None
        self.EsAcl = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.VpcUid = params.get("VpcUid")
        self.SubnetUid = params.get("SubnetUid")
        self.Status = params.get("Status")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.NodeNum = params.get("NodeNum")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.EsDomain = params.get("EsDomain")
        self.EsVip = params.get("EsVip")
        self.EsPort = params.get("EsPort")
        self.KibanaUrl = params.get("KibanaUrl")
        self.EsVersion = params.get("EsVersion")
        self.EsConfig = params.get("EsConfig")
        self.EsAcl = params.get("EsAcl")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 要重启的实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 要操作的实例ID
        :type InstanceId: str
        :param InstanceName: 修改后的实例名称
        :type InstanceName: str
        :param NodeNum: 横向扩缩容后的节点个数
        :type NodeNum: int
        :param EsConfig: 修改后的配置项
        :type EsConfig: str
        :param Password: 重置后的用户密码
        :type Password: str
        :param EsAcl: 修改后的访问控制列表
        :type EsAcl: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.NodeNum = None
        self.EsConfig = None
        self.Password = None
        self.EsAcl = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.EsConfig = params.get("EsConfig")
        self.Password = params.get("Password")
        self.EsAcl = params.get("EsAcl")


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")