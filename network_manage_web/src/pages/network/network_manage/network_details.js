import React, { Component, Fragment} from 'react'
import { actionCreators } from './store'
import { connect } from "react-redux";
import { Link } from 'react-router-dom'
import 'antd/dist/antd.css';
import { Table, Button, Space} from 'antd';


const pageSizeOptions = [30, 100, 500]

class NetworkDetail extends Component{
  render(){
    const columns = [
      {
        title: '网络地址',
        dataIndex: 'network',
        key: 'network',
        width: 100,
        ellipsis: true,
      },
      {
        title: 'IP地址',
        dataIndex: 'ip',
        key: 'ip',
        width: 100,
        sorter: true,
        ellipsis: true,
      },
      {
        title: 'IP地址状态',
        dataIndex: 'ip_status',
        key: 'ip_status',
        filters: [
          { text: '在线', value: '1' },
          { text: '离线', value: '0' },
        ],
        width: 100,
        ellipsis: true,
      },
      {
        title: '扫描MAC地址',
        dataIndex: 'scan_mac_address',
        key: 'scan_mac_address',
        width: 120,
        ellipsis: true,
      },
      {
        title: '扫描MAC地址厂商',
        dataIndex: 'scan_mac_product',
        key: 'scan_mac_product',
        width: 120,
        ellipsis: true,
      },
      {
        title: '手动MAC地址',
        dataIndex: 'manual_mac_address',
        key: 'manual_mac_address',
        width: 120,
        ellipsis: true,
      },
      {
        title: '手动MAC地址厂商',
        dataIndex: 'manual_mac_product',
        key: 'manual_mac_product',
        width: 120,
        ellipsis: true,
      },
      {
        title: '扫描设备接口',
        dataIndex: 'scan_device_port',
        key: 'scan_device_port',
        width: 120,
        ellipsis: true,
      },
      {
        title: '类型',
        dataIndex: 'ip_type',
        key: 'ip_type',
        width: 100,
        filters: [
          { text: '未管理', value: '0' },
          { text: '手动地址', value: '1' },
          { text: '未使用', value: '2' },
        ],
      },
    
      {
        title: 'TCP扫描端口',
        dataIndex: 'tcp_port_list',
        key: 'tcp_port_list',
        width: 120,
        ellipsis: true,
        render (text, record) {
          var value = []
          if(text !== ''){
            value = JSON.parse(text)
          }
          if(value.length >= 2){
            return (
              <Link to={'/network/network_details/tcp_port_list/tcp&'+record.ip}>{value.join("\n")}</Link>
            )
          }
          else{
            return(
              <div>{value.join(",")}</div>
            )
          }
        }
      },
      {
        title: 'UDP扫描端口',
        dataIndex: 'udp_port_list',
        key: 'udp_port_list',
        width: 120,
        ellipsis: true,
        render (text, record) {
          var value = []
          if(text !== ''){
            value = JSON.parse(text)
          }
          if(value.length >= 2){
            return (
              <Link to={'/network/network_details/udp_port_list/udp&'+record.ip}>{value.join("\n")}</Link>
            )
          }
          else{
            return(
              <div>{value.join(",")}</div>
            )
          }
        }
      },
      {
        title: '主机名',
        dataIndex: 'hostname',
        key: 'hostname',
        ellipsis: true,
        width: 100,
      },
      {
        title: '远程登陆',
        dataIndex: 'ssh',
        key: 'ssh',
        width: 160,
        render: (text, record) => 
        <Fragment>
          <Space>
            <Button>编辑</Button>
            <Button type='primary'>Console</Button>
          </Space>
        </Fragment>
        //  record是对象
      },
      {
        title: '活跃时间',
        dataIndex: 'active_time',
        key: 'active_time',
        width: 200,
      },
    ];

    const { } = this.props
    // NetworkQueryDetailsPagination["pageSizeOptions"] = pageSizeOptions
    // NetworkQueryDetailsPagination["showTotal"] = () => `总共${NetworkQueryDetailsPagination.total}条`
    const NetworkQueryDetailInfos = []
    return(
      <Fragment>
        <Table 
          columns={columns}
          dataSource={NetworkQueryDetailInfos} 
          bordered
          // pagination={ NetworkQueryDetailsPagination }
          onChange={(pagination, filters, sorter) => this.props.handleNetworkQueryDetailsTableChange(pagination, filters, sorter, this.props.match.params.id)}
        />
      </Fragment>
    )
  }
  componentDidMount(){
    console.log("this.props.match.params.id:", this.props.match.params.id)
    this.props.getNetworkIpDetailsInfo(this.props.match.params.id);
  }
}

const mapState = (state) => ({
  // consonleLoginVisible: state.getIn(['networkQuery', 'consonleLoginVisible']),
  // NetworkQueryDetailInfos: state.getIn(['networkQuery', 'NetworkQueryDetailInfos']),
  // NetworkQueryDetailsPagination: state.getIn(['networkQuery', 'NetworkQueryDetailsPagination']).toObject(),
})

const mapDispatch = (dispatch) =>({
  getNetworkIpDetailsInfo(id){
    var NetworkQueryDetailsPagination = {
      "pageSize": pageSizeOptions[0],
      "current": 1
    }
    dispatch(actionCreators.getNetworkIpDetailsInfo(id, NetworkQueryDetailsPagination))
  },
  // handleNetworkQueryDetailsTableChange(pagination, filters, sorter, id){
  //   dispatch(actionCreators.handleNetworkQueryDetailsTableChange(pagination, filters, sorter, id))
  // },
  // handleConsoleClick(ipAddress){
  //   dispatch(actionCreators.handleConsoleClick(ipAddress))
  // }
  
  })

export default connect(mapState, mapDispatch)(NetworkDetail)